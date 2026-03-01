from PyQt5 import QtCore, QtGui, QtWidgets
from concurrent.futures import ThreadPoolExecutor
import pyqtgraph
import numpy
import sql as s
import os


# Worker thread for database queries
class DatabaseWorker(QtCore.QThread):
    # Signals to send data back to main thread
    results_ready = QtCore.pyqtSignal(dict)
    error_occurred = QtCore.pyqtSignal(str)

    def __init__(self, fighter1, fighter2, map_name, matchType, season, month, week, ppv, championship, contender, brand):
        super().__init__()
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.map_name = map_name
        self.matchType = matchType
        self.season = season
        self.month = month
        self.week = week
        self.ppv = ppv
        self.championship = championship
        self.contender = contender
        self.brand = brand

    def run(self):
        try:
            results = {}

            # Individual Stats Queries (query, params)
            queries = [
                ("SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = %s AND Location_Name = %s", (self.fighter1, self.map_name)),
                ("SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = %s AND Location_Name = %s", (self.fighter2, self.map_name)),
                ("SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = %s AND FightType = %s", (self.fighter1, self.matchType)),
                ("SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = %s AND FightType = %s", (self.fighter2, self.matchType)),
                ("SELECT * FROM champfightstats WHERE Fighter_Name = %s", (self.fighter1,)),
                ("SELECT * FROM champfightstats WHERE Fighter_Name = %s", (self.fighter2,)),
                ("SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = %s AND PPV = %s", (self.fighter1, self.ppv)),
                ("SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = %s AND PPV = %s", (self.fighter2, self.ppv)),
                ("SELECT * FROM defendingtitle WHERE Fighter_Name = %s", (self.fighter1,)),
                ("SELECT * FROM defendingtitle WHERE Fighter_Name = %s", (self.fighter2,)),
                ("SELECT * FROM careerstats WHERE Fighter_Name = %s", (self.fighter1,)),
                ("SELECT * FROM careerstats WHERE Fighter_Name = %s", (self.fighter2,)),
                ("SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = %s AND Season = %s", (self.fighter1, self.season)),
                ("SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = %s AND Season = %s", (self.fighter2, self.season)),
                ("SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = %s AND Brand = %s", (self.fighter1, self.brand)),
                ("SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = %s AND Brand = %s", (self.fighter2, self.brand))
            ]

            # Head-to-head queries
            stored_procedures = [
                ("call SmashBros.headtohead(%s, %s)", (self.fighter1, self.fighter2)),
                ("call SmashBros.headtoheadLocation(%s, %s, %s)", (self.fighter1, self.fighter2, self.map_name)),
                ("call SmashBros.headtoheadFightType(%s, %s, %s)", (self.fighter1, self.fighter2, self.matchType)),
                ("call SmashBros.headtoheadSeason(%s, %s, %s)", (self.fighter1, self.fighter2, self.season)),
                ("call SmashBros.headtoheadMonth(%s, %s, %s)", (self.fighter1, self.fighter2, self.month)),
                ("call SmashBros.headtoheadChamp(%s, %s)", (self.fighter1, self.fighter2)),
                ("call SmashBros.headtoheadPPV(%s, %s, %s)", (self.fighter1, self.fighter2, self.ppv))
            ]

            # Fire all 23 queries in parallel -- each gets its own connection
            def run_individual(query_params):
                query, params = query_params
                try:
                    return s.select_view_row(query, params)
                except IndexError:
                    return None

            def run_h2h(proc_params):
                proc, params = proc_params
                return s.h2h_query_sql(proc, params)

            with ThreadPoolExecutor(max_workers=23) as pool:
                individual_futures = list(pool.map(run_individual, queries))
                h2h_futures = list(pool.map(run_h2h, stored_procedures))

            results['individual'] = individual_futures
            results['h2h'] = h2h_futures

            # Send results back to main thread
            self.results_ready.emit(results)

        except Exception as e:
            self.error_occurred.emit(str(e))


class Ui_SmashUI(object):
# Sets up the UI layout (used Qt Designer to set up layout)
    def setupUi(self, SmashUI):
        # Tab Widget Setup / Initialize Theme

        self.tabWidget = QtWidgets.QTabWidget(SmashUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1860, 1171))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'theme', 'darkeum.qss'), 'r', encoding='utf-8') as file:
            theme_content = file.read()
        self.tabWidget.setStyleSheet(theme_content)

        # Head to Head Tab

        self.HeadToHeadtab = QtWidgets.QWidget()
        self.HeadToHeadtab.setObjectName("HeadToHeadtab")
        self.tabWidget.addTab(self.HeadToHeadtab, "")

        # Fighter Table 2

        self.tableWidget2 = QtWidgets.QTableWidget(self.HeadToHeadtab)
        self.tableWidget2.setGeometry(QtCore.QRect(1118, 364, 690, 664))
        self.tableWidget2.setShowGrid(True)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)

        # Fighter Pictures and Text Boxes
                                            
        fighter_names = s.select_list("SELECT * FROM Fighter", 0)
        # Auto Complete for Fighter Names
        fighter_name_completer = QtWidgets.QCompleter(fighter_names)
        fighter_name_completer.setCaseSensitivity(0)
        fighter_name_completer.setCompletionMode(2)
        

        self.image1 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.image1.setGeometry(QtCore.QRect(273, 13, 287, 300))
        self.image1.setToolTipDuration(0)
        self.image1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image1.setText("")
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")

        self.FighterTextBox1 = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.FighterTextBox1.setGeometry(QtCore.QRect(312, 325, 209, 28))
        self.FighterTextBox1.setAlignment(QtCore.Qt.AlignCenter)
        self.FighterTextBox1.setObjectName("FighterTextBox1")
        self.FighterTextBox1.setCompleter(fighter_name_completer)

        self.image2 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.image2.setGeometry(QtCore.QRect(1313, 13, 287, 300))
        self.image2.setStyleSheet("")
        self.image2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image2.setText("")
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")

        self.FighterTextBox2 = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.FighterTextBox2.setGeometry(QtCore.QRect(1352, 325, 209, 28))
        self.FighterTextBox2.setFrame(True)
        self.FighterTextBox2.setAlignment(QtCore.Qt.AlignCenter)
        self.FighterTextBox2.setObjectName("FighterTextBox2")
        self.FighterTextBox2.setCompleter(fighter_name_completer)

        # Stage Images and Text Boxes

        location_list = s.select_list('SELECT * FROM Location', 1)
        location_list_completer = QtWidgets.QCompleter(location_list)
        location_list_completer.setCaseSensitivity(0)

        self.MapTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MapTextBox.setGeometry(QtCore.QRect(819, 325, 222, 28))
        self.MapTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MapTextBox.setObjectName("MapTextBox")
        self.MapTextBox.setCompleter(location_list_completer)

        self.imageStage = QtWidgets.QLabel(self.HeadToHeadtab)
        self.imageStage.setGeometry(QtCore.QRect(637, 13, 586, 300))
        self.imageStage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageStage.setText("")
        self.imageStage.setScaledContents(True)
        self.imageStage.setObjectName("imageStage")

        # Labels and Data Text Boxes

        self.label = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label.setGeometry(QtCore.QRect(741, 325, 78, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_2.setGeometry(QtCore.QRect(741, 377, 78, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_3.setGeometry(QtCore.QRect(741, 429, 78, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        fightType_list = s.select_list('SELECT * FROM FightType', 1)
        fightType_list_completer = QtWidgets.QCompleter(fightType_list)
        fightType_list_completer.setCaseSensitivity(0)
        fightType_list_completer.setCompletionMode(1)

        self.MatchTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MatchTextBox.setGeometry(QtCore.QRect(819, 377, 222, 28))
        self.MatchTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MatchTextBox.setObjectName("MatchTextBox")
        self.MatchTextBox.setCompleter(fightType_list_completer)

        self.SeasonTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.SeasonTextBox.setGeometry(QtCore.QRect(819, 429, 222, 28))
        self.SeasonTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.SeasonTextBox.setObjectName("SeasonTextBox")

        self.MonthTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MonthTextBox.setGeometry(QtCore.QRect(819, 481, 222, 28))
        self.MonthTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MonthTextBox.setObjectName("MonthTextBox")

        self.label_4 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_4.setGeometry(QtCore.QRect(741, 481, 78, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.WeekTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.WeekTextBox.setGeometry(QtCore.QRect(819, 533, 222, 28))
        self.WeekTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WeekTextBox.setObjectName("WeekTextBox")

        self.label_5 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_5.setGeometry(QtCore.QRect(741, 533, 78, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        ppv_list = s.select_list('SELECT * FROM PPV', 1)
        ppv_list_completer = QtWidgets.QCompleter(ppv_list)
        ppv_list_completer.setCaseSensitivity(0)
        ppv_list_completer.setCompletionMode(1)

        self.PPVTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.PPVTextBox.setGeometry(QtCore.QRect(819, 585, 222, 28))
        self.PPVTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PPVTextBox.setObjectName("PPVTextBox")
        self.PPVTextBox.setCompleter(ppv_list_completer)

        self.label_6 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_6.setGeometry(QtCore.QRect(741, 585, 78, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        champ_list = s.select_list('SELECT * FROM Championship', 1)
        champ_list_completer = QtWidgets.QCompleter(champ_list)
        champ_list_completer.setCaseSensitivity(0)
        champ_list_completer.setCompletionMode(1)

        self.ChampTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ChampTextBox.setGeometry(QtCore.QRect(819, 637, 222, 28))
        self.ChampTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ChampTextBox.setObjectName("ChampTextBox")
        self.ChampTextBox.setCompleter(champ_list_completer)

        self.label_7 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_7.setGeometry(QtCore.QRect(741, 637, 78, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.ContenderTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ContenderTextBox.setGeometry(QtCore.QRect(819, 689, 222, 28))
        self.ContenderTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ContenderTextBox.setObjectName("ContenderTextBox")

        self.label_8 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_8.setGeometry(QtCore.QRect(741, 689, 78, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        brand_list = s.select_list('SELECT * FROM Brand', 1)
        brand_list_completer = QtWidgets.QCompleter(brand_list)
        brand_list_completer.setCaseSensitivity(0)
        brand_list_completer.setCompletionMode(1)

        self.BrandTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.BrandTextBox.setGeometry(QtCore.QRect(819, 741, 222, 28))
        self.BrandTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.BrandTextBox.setObjectName("BrandTextBox")
        self.BrandTextBox.setCompleter(brand_list_completer)

        self.label_9 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_9.setGeometry(QtCore.QRect(741, 741, 78, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.ErrorTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ErrorTextBox.setGeometry(QtCore.QRect(819, 871, 222, 28))
        self.ErrorTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorTextBox.setObjectName("ErrorTextBox")

        self.label_10 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_10.setGeometry(QtCore.QRect(741, 871, 78, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

         # Check Stats Button
        self.CheckStatsButton = QtWidgets.QPushButton(self.HeadToHeadtab)
        self.CheckStatsButton.setGeometry(QtCore.QRect(845, 793, 170, 53))
        self.CheckStatsButton.setObjectName("CheckStatsButton")
        self.CheckStatsButton.clicked.connect(self.checkStats)
        self.CheckStatsButton.setStyleSheet("background-color : gray")
        
         # Clear Button
        self.ClearButton = QtWidgets.QPushButton(self.HeadToHeadtab)
        self.ClearButton.setGeometry(QtCore.QRect(845, 923, 170, 53))
        self.ClearButton.setObjectName("ClearButton")
        self.ClearButton.clicked.connect(self.clear)
        self.ClearButton.setStyleSheet("background-color : gray")


        # Fighter Table 1
        self.tableWidget1 = QtWidgets.QTableWidget(self.HeadToHeadtab)
        self.tableWidget1.setGeometry(QtCore.QRect(39, 364, 690, 664))
        self.tableWidget1.setShowGrid(True)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)

        # Wide row header for text labels, data columns stretch to fill the rest
        for table in (self.tableWidget1, self.tableWidget2):
            table.verticalHeader().setFixedWidth(400)
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Set Tables with Default Values

        for row in range(0,15):
            for table in (self.tableWidget1, self.tableWidget2):
                for col, val in enumerate(['0', '0', '0.00%']):
                    item = QtWidgets.QTableWidgetItem(val)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    table.setItem(row, col, item)

        # Load Data (ETL) Tab
        self.LoadDataTab = QtWidgets.QWidget()
        self.LoadDataTab.setObjectName("LoadDataTab")
        self.tabWidget.addTab(self.LoadDataTab, "")

        # Advanced Stats Tab
        self.AdvancedStatsTab = QtWidgets.QWidget()
        self.AdvancedStatsTab.setObjectName("AdvancedStatsTab")
        self.tabWidget.addTab(self.AdvancedStatsTab, "")

        # Graphs Tab
        self.GraphTab = QtWidgets.QWidget()
        self.GraphTab.setObjectName("GraphTab")
        self.tabWidget.addTab(self.GraphTab, "")

        # Functionality
        self.retranslateUi(SmashUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SmashUI)

# Labels the UI
    def retranslateUi(self, SmashUI):
        _translate = QtCore.QCoreApplication.translate
        SmashUI.setWindowTitle(_translate("SmashUI", "Super Smash Bros"))
        item = self.tableWidget2.verticalHeaderItem(0)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (Total)"))
        item = self.tableWidget2.verticalHeaderItem(1)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (At Location)"))
        item = self.tableWidget2.verticalHeaderItem(2)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (Match Type)"))
        item = self.tableWidget2.verticalHeaderItem(3)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (in the Season of)"))
        item = self.tableWidget2.verticalHeaderItem(4)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (in the Month of)"))
        item = self.tableWidget2.verticalHeaderItem(5)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (for Championship)"))
        item = self.tableWidget2.verticalHeaderItem(6)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (at PPV)"))
        item = self.tableWidget2.verticalHeaderItem(7)
        item.setText(_translate("SmashUI", "at Location"))
        item = self.tableWidget2.verticalHeaderItem(8)
        item.setText(_translate("SmashUI", "for Match Type"))
        item = self.tableWidget2.verticalHeaderItem(9)
        item.setText(_translate("SmashUI", "in Championship matches"))
        item = self.tableWidget2.verticalHeaderItem(10)
        item.setText(_translate("SmashUI", "at PPV"))
        item = self.tableWidget2.verticalHeaderItem(11)
        item.setText(_translate("SmashUI", "when Defending a Title"))
        item = self.tableWidget2.verticalHeaderItem(12)
        item.setText(_translate("SmashUI", "Total Record"))
        item = self.tableWidget2.verticalHeaderItem(13)
        item.setText(_translate("SmashUI", "Season Record"))
        item = self.tableWidget2.verticalHeaderItem(14)
        item.setText(_translate("SmashUI", "On Brand"))
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("SmashUI", "Wins"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("SmashUI", "Losses"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("SmashUI", "W/L %"))
        self.FighterTextBox2.setText(_translate("SmashUI", "Enter Fighter"))
        self.FighterTextBox1.setText(_translate("SmashUI", "Enter Fighter"))
        self.MapTextBox.setText(_translate("SmashUI", "Enter Map"))
        self.label.setText(_translate("SmashUI", "Map:"))
        self.label_2.setText(_translate("SmashUI", "MT:"))
        self.label_3.setText(_translate("SmashUI", "Season:"))
        self.SeasonTextBox.setText(_translate("SmashUI", "Enter Season"))
        self.MatchTextBox.setText(_translate("SmashUI", "Enter Match Type"))
        self.MonthTextBox.setText(_translate("SmashUI", "Enter Month Number"))
        self.label_4.setText(_translate("SmashUI", "Month:"))
        self.WeekTextBox.setText(_translate("SmashUI", "Enter Week"))
        self.label_5.setText(_translate("SmashUI", "Week:"))
        self.PPVTextBox.setText(_translate("SmashUI", "Enter PPV Name"))
        self.label_6.setText(_translate("SmashUI", "PPV:"))
        self.ChampTextBox.setText(_translate("SmashUI", "Enter Championship"))
        self.label_7.setText(_translate("SmashUI", "Champ:"))
        self.ContenderTextBox.setText(_translate("SmashUI", "#1 Contender Match?"))
        self.label_8.setText(_translate("SmashUI", "#1con:"))
        self.BrandTextBox.setText(_translate("SmashUI", "Enter Brand"))
        self.label_9.setText(_translate("SmashUI", "Brand:"))
        self.CheckStatsButton.setText(_translate("SmashUI", "Check Stats"))
        self.ClearButton.setText(_translate("SmashUI","Clear"))
        self.ErrorTextBox.setText(_translate("SmashUI", ""))
        self.label_10.setText(_translate("SmashUI", "Error:"))
        item = self.tableWidget1.verticalHeaderItem(0)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (Total)"))
        item = self.tableWidget1.verticalHeaderItem(1)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (At Location)"))
        item = self.tableWidget1.verticalHeaderItem(2)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (Match Type)"))
        item = self.tableWidget1.verticalHeaderItem(3)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (in the Season of)"))
        item = self.tableWidget1.verticalHeaderItem(4)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (in the Month of)"))
        item = self.tableWidget1.verticalHeaderItem(5)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (for Championship)"))
        item = self.tableWidget1.verticalHeaderItem(6)
        item.setText(_translate("SmashUI", "Vs.  Other Fighter (at PPV)"))
        item = self.tableWidget1.verticalHeaderItem(7)
        item.setText(_translate("SmashUI", "at Location"))
        item = self.tableWidget1.verticalHeaderItem(8)
        item.setText(_translate("SmashUI", "for Match Type"))
        item = self.tableWidget1.verticalHeaderItem(9)
        item.setText(_translate("SmashUI", "in Championship matches"))
        item = self.tableWidget1.verticalHeaderItem(10)
        item.setText(_translate("SmashUI", "at PPV"))
        item = self.tableWidget1.verticalHeaderItem(11)
        item.setText(_translate("SmashUI", "when Defending a Title"))
        item = self.tableWidget1.verticalHeaderItem(12)
        item.setText(_translate("SmashUI", "Total Record"))
        item = self.tableWidget1.verticalHeaderItem(13)
        item.setText(_translate("SmashUI", "Season Record"))
        item = self.tableWidget1.verticalHeaderItem(14)
        item.setText(_translate("SmashUI", "On Brand"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("SmashUI", "Wins"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("SmashUI", "Losses"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("SmashUI", "W/L %"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HeadToHeadtab), _translate("SmashUI", "Head to Head"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LoadDataTab), _translate("SmashUI", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AdvancedStatsTab), _translate("SmashUI", "Advanced Fighter Stats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GraphTab), _translate("SmashUI", "Graphs"))

# Clear Button in UI

    def clear(self):
        # When you click clear, set GUI back to intial state. 
        self.FighterTextBox2.setText("Enter Fighter")
        self.FighterTextBox1.setText("Enter Fighter")
        self.MapTextBox.setText("Enter Map")
        self.SeasonTextBox.setText("Enter Season")
        self.MatchTextBox.setText("Enter Match Type")
        self.MonthTextBox.setText("Enter Month Number")
        self.WeekTextBox.setText("Enter Week")
        self.PPVTextBox.setText("Enter PPV Name")
        self.ChampTextBox.setText("Enter Championship")
        self.ContenderTextBox.setText("#1 Contender Match?")
        self.BrandTextBox.setText("Enter Brand")

        # Empty pictures
        self.image1.setPixmap(QtGui.QPixmap(""))
        self.image2.setPixmap(QtGui.QPixmap(""))
        self.imageStage.setPixmap(QtGui.QPixmap(""))

        # Change all numbers in data table to 0 or 0%
        for row in range(0,15):
            for table in (self.tableWidget1, self.tableWidget2):
                for col, val in enumerate(['0', '0', '0.00%']):
                    item = QtWidgets.QTableWidgetItem(val)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    table.setItem(row, col, item)

# Check Stats Button in UI

    def checkStats(self):
        # Show loading cursor
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        # Disable button while loading
        self.CheckStatsButton.setEnabled(False)
        self.CheckStatsButton.setText("Loading...")
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Change Pictures based on input in the fighter/stage text box
        fighter1_filename = self.FighterTextBox1.text().lower().replace(' ', '').replace('.','').replace('&', 'and')
        fighter2_filename = self.FighterTextBox2.text().lower().replace(' ', '').replace('.','').replace('&','and')
        stage_filename = self.MapTextBox.text().lower().replace(' ','').replace(',','').replace("'",'').replace('(','').replace(')','').replace('-','')

        self.image1.setPixmap(QtGui.QPixmap(os.path.join(script_dir, 'assets', 'fighters', f'{fighter1_filename}.png')))
        self.image2.setPixmap(QtGui.QPixmap(os.path.join(script_dir, 'assets', 'fighters', f'{fighter2_filename}.png')))
        self.imageStage.setPixmap(QtGui.QPixmap(os.path.join(script_dir, 'assets', 'stages', f'{stage_filename}.png')))
        
        # Initialize Variables
        fighter1 = self.FighterTextBox1.text()
        fighter2 = self.FighterTextBox2.text()
        map_name = self.MapTextBox.text()
        matchType = self.MatchTextBox.text()
        season = self.SeasonTextBox.text()
        month = self.MonthTextBox.text()
        week = self.WeekTextBox.text()
        ppv = self.PPVTextBox.text()
        championship = self.ChampTextBox.text()
        contender = self.ContenderTextBox.text()
        brand = self.BrandTextBox.text()

        # Validate inputs
        if fighter1 == 'Enter Fighter' or fighter2 == 'Enter Fighter':
            self.ErrorTextBox.setText('Enter Another Fighter!')
            QtWidgets.QApplication.restoreOverrideCursor()
            self.CheckStatsButton.setEnabled(True)
            self.CheckStatsButton.setText("Check Stats")
            return

        # Create and start worker thread
        self.worker = DatabaseWorker(fighter1, fighter2, map_name, matchType, season, month, week, ppv, championship, contender, brand)
        self.worker.results_ready.connect(self.handle_results)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.start()

    def handle_error(self, error_msg):
        self.ErrorTextBox.setText(f'Error: {error_msg}')
        QtWidgets.QApplication.restoreOverrideCursor()
        self.CheckStatsButton.setEnabled(True)
        self.CheckStatsButton.setText("Check Stats")

    def _centered_item(self, text):
        item = QtWidgets.QTableWidgetItem(str(text))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        return item

    def handle_results(self, results):
        # Process individual stats
        indy_widget_row_fighter_1 = 7
        indy_widget_row_fighter_2 = 7

        for i, data in enumerate(results['individual']):
            # Fighter 1's queries (even indices)
            if i % 2 == 0:
                if data and len(data) > 0:
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 0, self._centered_item(data[0][-3]))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 1, self._centered_item(data[0][-2]))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 2, self._centered_item(data[0][-1]))
                else:
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 0, self._centered_item('0'))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 1, self._centered_item('0'))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1, 2, self._centered_item('0.00%'))
                indy_widget_row_fighter_1 += 1
            # Fighter 2's queries (odd indices)
            else:
                if data and len(data) > 0:
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 0, self._centered_item(data[0][-3]))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 1, self._centered_item(data[0][-2]))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 2, self._centered_item(data[0][-1]))
                else:
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 0, self._centered_item('0'))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 1, self._centered_item('0'))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2, 2, self._centered_item('0.00%'))
                indy_widget_row_fighter_2 += 1

        # Process head-to-head stats
        h2h_widget_row = 0
        for dataH2H in results['h2h']:
            self.tableWidget1.setItem(h2h_widget_row, 0, self._centered_item(dataH2H[0]['Wins']))
            self.tableWidget1.setItem(h2h_widget_row, 1, self._centered_item(dataH2H[0]['Losses']))
            self.tableWidget1.setItem(h2h_widget_row, 2, self._centered_item(dataH2H[0]['W/L %']))

            self.tableWidget2.setItem(h2h_widget_row, 0, self._centered_item(dataH2H[1]['Wins']))
            self.tableWidget2.setItem(h2h_widget_row, 1, self._centered_item(dataH2H[1]['Losses']))
            self.tableWidget2.setItem(h2h_widget_row, 2, self._centered_item(dataH2H[1]['W/L %']))
            h2h_widget_row += 1

        # Clear error and restore UI
        self.ErrorTextBox.setText('')
        QtWidgets.QApplication.restoreOverrideCursor()
        self.CheckStatsButton.setEnabled(True)
        self.CheckStatsButton.setText("Check Stats")
        
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmashUI = QtWidgets.QDialog()
    ui = Ui_SmashUI()
    ui.setupUi(SmashUI)
    SmashUI.setWindowTitle("Super Smash Bros Stats")

    # Fixed size optimized for MacBook Pro (bigger than original 1431x901)
    # This works well on 14"/16" MacBook Pro and external monitors
    SmashUI.setFixedSize(1800, 1171)  # Slightly reduced to fit W/L % column

    SmashUI.show()
    sys.exit(app.exec_())
