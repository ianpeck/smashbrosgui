from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph
import numpy
import sql as s


class Ui_SmashUI(object):
# Sets up the UI layout (used Qt Designer to set up layout)
    def setupUi(self, SmashUI):
        # Tab Widget Setup / Initialize Theme

        self.tabWidget = QtWidgets.QTabWidget(SmashUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1431, 901))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        with open('theme/darkeum.qss', 'r', encoding='utf-8') as file:
            str = file.read()
        self.tabWidget.setStyleSheet(str)

        # Head to Head Tab

        self.HeadToHeadtab = QtWidgets.QWidget()
        self.HeadToHeadtab.setObjectName("HeadToHeadtab")
        self.tabWidget.addTab(self.HeadToHeadtab, "")

        # Fighter Table 2

        self.tableWidget2 = QtWidgets.QTableWidget(self.HeadToHeadtab)
        self.tableWidget2.setGeometry(QtCore.QRect(860, 280, 531, 511))
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
        self.image1.setGeometry(QtCore.QRect(210, 10, 221, 231))
        self.image1.setToolTipDuration(0)
        self.image1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image1.setText("")
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")

        self.FighterTextBox1 = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.FighterTextBox1.setGeometry(QtCore.QRect(240, 250, 161, 22))
        self.FighterTextBox1.setAlignment(QtCore.Qt.AlignCenter)
        self.FighterTextBox1.setObjectName("FighterTextBox1")
        self.FighterTextBox1.setCompleter(fighter_name_completer)

        self.image2 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.image2.setGeometry(QtCore.QRect(1010, 10, 221, 231))
        self.image2.setStyleSheet("")
        self.image2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image2.setText("")
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")

        self.FighterTextBox2 = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.FighterTextBox2.setGeometry(QtCore.QRect(1040, 250, 161, 22))
        self.FighterTextBox2.setFrame(True)
        self.FighterTextBox2.setAlignment(QtCore.Qt.AlignCenter)
        self.FighterTextBox2.setObjectName("FighterTextBox2")
        self.FighterTextBox2.setCompleter(fighter_name_completer)

        # Stage Images and Text Boxes

        location_list = s.select_list('SELECT * FROM Location', 1)
        location_list_completer = QtWidgets.QCompleter(location_list)
        location_list_completer.setCaseSensitivity(0)

        self.MapTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MapTextBox.setGeometry(QtCore.QRect(630, 250, 171, 22))
        self.MapTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MapTextBox.setObjectName("MapTextBox")
        self.MapTextBox.setCompleter(location_list_completer)

        self.imageStage = QtWidgets.QLabel(self.HeadToHeadtab)
        self.imageStage.setGeometry(QtCore.QRect(490, 10, 451, 231))
        self.imageStage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageStage.setText("")
        self.imageStage.setScaledContents(True)
        self.imageStage.setObjectName("imageStage")

        # Labels and Data Text Boxes

        self.label = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label.setGeometry(QtCore.QRect(570, 250, 60, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_2.setGeometry(QtCore.QRect(570, 290, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_3.setGeometry(QtCore.QRect(570, 330, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        fightType_list = s.select_list('SELECT * FROM FightType', 1)
        fightType_list_completer = QtWidgets.QCompleter(fightType_list)
        fightType_list_completer.setCaseSensitivity(0)
        fightType_list_completer.setCompletionMode(1)

        self.MatchTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MatchTextBox.setGeometry(QtCore.QRect(630, 290, 171, 22))
        self.MatchTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MatchTextBox.setObjectName("MatchTextBox")
        self.MatchTextBox.setCompleter(fightType_list_completer)

        self.SeasonTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.SeasonTextBox.setGeometry(QtCore.QRect(630, 330, 171, 22))
        self.SeasonTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.SeasonTextBox.setObjectName("SeasonTextBox")

        self.MonthTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.MonthTextBox.setGeometry(QtCore.QRect(630, 370, 171, 22))
        self.MonthTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MonthTextBox.setObjectName("MonthTextBox")

        self.label_4 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_4.setGeometry(QtCore.QRect(570, 370, 60, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.WeekTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.WeekTextBox.setGeometry(QtCore.QRect(630, 410, 171, 22))
        self.WeekTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WeekTextBox.setObjectName("WeekTextBox")

        self.label_5 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_5.setGeometry(QtCore.QRect(570, 410, 60, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        ppv_list = s.select_list('SELECT * FROM PPV', 1)
        ppv_list_completer = QtWidgets.QCompleter(ppv_list)
        ppv_list_completer.setCaseSensitivity(0)
        ppv_list_completer.setCompletionMode(1)

        self.PPVTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.PPVTextBox.setGeometry(QtCore.QRect(630, 450, 171, 22))
        self.PPVTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PPVTextBox.setObjectName("PPVTextBox")
        self.PPVTextBox.setCompleter(ppv_list_completer)

        self.label_6 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_6.setGeometry(QtCore.QRect(570, 450, 60, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        champ_list = s.select_list('SELECT * FROM Championship', 1)
        champ_list_completer = QtWidgets.QCompleter(champ_list)
        champ_list_completer.setCaseSensitivity(0)
        champ_list_completer.setCompletionMode(1)

        self.ChampTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ChampTextBox.setGeometry(QtCore.QRect(630, 490, 171, 22))
        self.ChampTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ChampTextBox.setObjectName("ChampTextBox")
        self.ChampTextBox.setCompleter(champ_list_completer)

        self.label_7 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_7.setGeometry(QtCore.QRect(570, 490, 60, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.ContenderTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ContenderTextBox.setGeometry(QtCore.QRect(630, 530, 171, 22))
        self.ContenderTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ContenderTextBox.setObjectName("ContenderTextBox")

        self.label_8 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_8.setGeometry(QtCore.QRect(570, 530, 60, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        brand_list = s.select_list('SELECT * FROM Brand', 1)
        brand_list_completer = QtWidgets.QCompleter(brand_list)
        brand_list_completer.setCaseSensitivity(0)
        brand_list_completer.setCompletionMode(1)

        self.BrandTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.BrandTextBox.setGeometry(QtCore.QRect(630, 570, 171, 22))
        self.BrandTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.BrandTextBox.setObjectName("BrandTextBox")
        self.BrandTextBox.setCompleter(brand_list_completer)

        self.label_9 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_9.setGeometry(QtCore.QRect(570, 570, 60, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.ErrorTextBox = QtWidgets.QLineEdit(self.HeadToHeadtab)
        self.ErrorTextBox.setGeometry(QtCore.QRect(630, 670, 171, 22))
        self.ErrorTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorTextBox.setObjectName("ErrorTextBox")

        self.label_10 = QtWidgets.QLabel(self.HeadToHeadtab)
        self.label_10.setGeometry(QtCore.QRect(570, 670, 60, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

         # Check Stats Button
        self.CheckStatsButton = QtWidgets.QPushButton(self.HeadToHeadtab)
        self.CheckStatsButton.setGeometry(QtCore.QRect(650, 610, 131, 41))
        self.CheckStatsButton.setObjectName("CheckStatsButton")
        self.CheckStatsButton.clicked.connect(self.checkStats)
        self.CheckStatsButton.setStyleSheet("background-color : gray")
        
         # Clear Button
        self.ClearButton = QtWidgets.QPushButton(self.HeadToHeadtab)
        self.ClearButton.setGeometry(QtCore.QRect(650, 710, 131, 41))
        self.ClearButton.setObjectName("ClearButton")
        self.ClearButton.clicked.connect(self.clear)
        self.ClearButton.setStyleSheet("background-color : gray")


        # Fighter Table 1
        self.tableWidget1 = QtWidgets.QTableWidget(self.HeadToHeadtab)
        self.tableWidget1.setGeometry(QtCore.QRect(30, 280, 531, 511))
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

        # Set Tables with Default Values

        for row in range(0,15):
            self.tableWidget1.setItem(row,0,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget1.setItem(row,1,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget1.setItem(row,2,QtWidgets.QTableWidgetItem('0.00%'))
            self.tableWidget2.setItem(row,0,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget2.setItem(row,1,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget2.setItem(row,2,QtWidgets.QTableWidgetItem('0.00%'))
        
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
            self.tableWidget1.setItem(row,0,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget1.setItem(row,1,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget1.setItem(row,2,QtWidgets.QTableWidgetItem('0.00%'))
            self.tableWidget2.setItem(row,0,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget2.setItem(row,1,QtWidgets.QTableWidgetItem('0'))
            self.tableWidget2.setItem(row,2,QtWidgets.QTableWidgetItem('0.00%'))

# Check Stats Button in UI

    def checkStats(self):
        # Change Pictures based on input in the fighter/stage text box
        self.image1.setPixmap(QtGui.QPixmap("/Users/ianjpeck/Documents/GitHub/smashbrosgui/fighterpictures/{}.png".format(self.FighterTextBox1.text().lower().replace(' ', '').replace('.','').replace('&', 'and'))))
        self.image2.setPixmap(QtGui.QPixmap("/Users/ianjpeck/Documents/GitHub/smashbrosgui/fighterpictures/{}.png".format(self.FighterTextBox2.text().lower().replace(' ', '').replace('.','').replace('&','and'))))
        self.imageStage.setPixmap(QtGui.QPixmap("/Users/ianjpeck/Documents/GitHub/smashbrosgui/stagepictures/{}.png".format(self.MapTextBox.text().lower().replace(' ','').replace(',','').replace("'",'').replace('(','').replace(')','').replace('-',''))))
        
        # Initialize Variables
        fighter1 = self.FighterTextBox1.text()
        fighter2 = self.FighterTextBox2.text()
        map = self.MapTextBox.text()
        matchType = self.MatchTextBox.text()
        season = self.SeasonTextBox.text()
        month = self.MonthTextBox.text()
        week = self.WeekTextBox.text()
        ppv = self.PPVTextBox.text()
        championship = self.ChampTextBox.text()
        contender = self.ContenderTextBox.text()
        brand = self.BrandTextBox.text()
        dataIndy = []
        dataH2H = []
        fighter_names = s.select_list('SELECT * FROM Fighter', 0)

        # Individual Stats Queries
        queries = ["SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{}' AND Location_Name = '{}'".format(fighter1, map.replace("'","''")),
        "SELECT * FROM CareerStatsByLocation WHERE Fighter_Name = '{}' AND Location_Name = '{}'".format(fighter2, map.replace("'","''")),
        "SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = '{}' AND FightType = '{}'".format(fighter1, matchType),
        "SELECT * FROM CareerStatsByFightType WHERE Fighter_Name = '{}' AND FightType = '{}'".format(fighter2, matchType),
        "SELECT * FROM champfightstats WHERE Fighter_Name = '{}'".format(fighter1),
        "SELECT * FROM champfightstats WHERE Fighter_Name = '{}'".format(fighter2),
        "SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = '{}' AND PPV = '{}'".format(fighter1, ppv),
        "SELECT * FROM CareerStatsByPPV WHERE Fighter_Name = '{}' AND PPV = '{}'".format(fighter2, ppv),
        "SELECT * FROM defendingtitle WHERE Fighter_Name = '{}'".format(fighter1),
        "SELECT * FROM defendingtitle WHERE Fighter_Name = '{}'".format(fighter2),
        "SELECT * FROM careerstats WHERE Fighter_Name = '{}'".format(fighter1),
        "SELECT * FROM careerstats WHERE Fighter_Name = '{}'".format(fighter2),
        "SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = '{}' AND Season = '{}'".format(fighter1, season),
        "SELECT * FROM CareerStatsBySeason WHERE Fighter_Name = '{}' AND Season = '{}'".format(fighter2, season),
        "SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = '{}' AND Brand = '{}'".format(fighter1, brand),
        "SELECT * FROM CareerStatsByBrand WHERE Fighter_Name = '{}' AND Brand = '{}'".format(fighter2, brand)]

        # First Row of Individual Stats starts at 7
        indy_widget_row_fighter_1 = 7
        indy_widget_row_fighter_2 = 7

        # Loops through our queries list and runs them, assigns the results to their correct spots in the GUI data table
        for i, query in enumerate(queries):

        # Fighter 1's queries, if there is no Fighter 1, error will be caught and 0's will be assigned to Wins/Losses/Win %
            if i % 2 == 0:

                try:

                    data_fighter_1 = s.select_view_row(query)

                    # Wins
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,0,QtWidgets.QTableWidgetItem(str(data_fighter_1[0][-3])))
                    # Losses
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,1,QtWidgets.QTableWidgetItem(str(data_fighter_1[0][-2])))
                    # Win Percentage
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,2,QtWidgets.QTableWidgetItem(data_fighter_1[0][-1]))
                    indy_widget_row_fighter_1 += 1
                    
                except IndexError:
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,0,QtWidgets.QTableWidgetItem('0'))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,1,QtWidgets.QTableWidgetItem('0'))
                    self.tableWidget1.setItem(indy_widget_row_fighter_1,2,QtWidgets.QTableWidgetItem('0.00%'))
                    indy_widget_row_fighter_1 += 1
                    pass
                    


            else:

                try:

                    data_fighter_2 = s.select_view_row(query)

                    self.tableWidget2.setItem(indy_widget_row_fighter_2,0,QtWidgets.QTableWidgetItem(str(data_fighter_2[0][-3])))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2,1,QtWidgets.QTableWidgetItem(str(data_fighter_2[0][-2])))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2,2,QtWidgets.QTableWidgetItem(data_fighter_2[0][-1]))
                    indy_widget_row_fighter_2 += 1
                    
                except IndexError:
                    self.tableWidget2.setItem(indy_widget_row_fighter_2,0,QtWidgets.QTableWidgetItem('0'))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2,1,QtWidgets.QTableWidgetItem('0'))
                    self.tableWidget2.setItem(indy_widget_row_fighter_2,2,QtWidgets.QTableWidgetItem('0.00%'))
                    indy_widget_row_fighter_2 += 1
                    pass

        
        # Vs. Other Fighter (All Rows)
        stored_procedures = ["call SmashBros.headtohead('{}','{}');".format(fighter1, fighter2), 
        "call SmashBros.headtoheadLocation('{}','{}','{}');".format(fighter1, fighter2, map.replace("'","''")),
        "call SmashBros.headtoheadFightType('{}','{}','{}');".format(fighter1, fighter2, matchType),
        "call SmashBros.headtoheadSeason('{}','{}','{}');".format(fighter1, fighter2, season), 
        "call SmashBros.headtoheadMonth('{}','{}','{}');".format(fighter1, fighter2, month), 
        "call SmashBros.headtoheadChamp('{}','{}');".format(fighter1, fighter2), 
        "call SmashBros.headtoheadPPV('{}','{}','{}');".format(fighter1, fighter2, ppv)]

        # Row Number starts at 0 since H2H stats are at the top of the data table in the GUI
        h2h_widget_row = 0

        # Only attempts to run this if both text boxes are not equal to the original text the GUI assigns originally to the text box
        if fighter1 and fighter2 != 'Enter Fighter':
            for stored_procedure in stored_procedures:
                dataH2H = s.h2h_query_sql("{}".format(stored_procedure))
                
                self.tableWidget1.setItem(h2h_widget_row,0,QtWidgets.QTableWidgetItem(dataH2H[0]['Wins']))
                self.tableWidget1.setItem(h2h_widget_row,1,QtWidgets.QTableWidgetItem(dataH2H[0]['Losses']))
                self.tableWidget1.setItem(h2h_widget_row,2,QtWidgets.QTableWidgetItem(dataH2H[0]['W/L %']))

                self.tableWidget2.setItem(h2h_widget_row,0,QtWidgets.QTableWidgetItem(dataH2H[1]['Wins']))
                self.tableWidget2.setItem(h2h_widget_row,1,QtWidgets.QTableWidgetItem(dataH2H[1]['Losses']))
                self.tableWidget2.setItem(h2h_widget_row,2,QtWidgets.QTableWidgetItem(dataH2H[1]['W/L %']))
                self.ErrorTextBox.setText('')
                h2h_widget_row += 1
        elif fighter1 or fighter2 == 'Enter Fighter':
            self.ErrorTextBox.setText('Enter Another Fighter!')
        elif fighter1 or fighter2 not in fighter_names:
            self.ErrorTextBox.setText('Enter Valid Fighter!')
        
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmashUI = QtWidgets.QDialog()
    ui = Ui_SmashUI()
    ui.setupUi(SmashUI)
    SmashUI.show()
    sys.exit(app.exec_())
