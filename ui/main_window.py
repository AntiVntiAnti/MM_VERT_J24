import datetime
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate, QSettings, QTime, Qt, QByteArray, QDateTime
from PyQt6.QtGui import QCloseEvent

import tracker_config as tkc
# ////////////////////////////////////////////////////////////////////////////////////////
# UI
# ////////////////////////////////////////////////////////////////////////////////////////
from ui.main_ui.gui import Ui_MainWindow

# ////////////////////////////////////////////////////////////////////////////////////////
# LOGGER
# ////////////////////////////////////////////////////////////////////////////////////////
from logger_setup import logger

# ////////////////////////////////////////////////////////////////////////////////////////
# NAVIGATION
# ////////////////////////////////////////////////////////////////////////////////////////
from navigation.master_navigation import change_stack_page

# Window geometry and frame
from utility.app_operations.frameless_window import (
    FramelessWindow)
from utility.app_operations.window_controls import (
    WindowController)
from utility.app_operations.show_hide import toggle_views
# app ops
from utility.widgets_set_widgets.slider_spinbox_connections import (
    connect_slider_spinbox)

# ////////////////////////////////////////////////////////////////////////////////////////
# DATABASE Magicks w/ Wizardry & Necromancy
# ////////////////////////////////////////////////////////////////////////////////////////
# Database connections
from database.database_manager import (
    DataManager)

# Delete Records
from database.database_utility.delete_records import (
    delete_selected_rows)

# setup Models
from database.database_utility.model_setup import (
    create_and_set_model)

# ////////////////////////////////////////////////////////////////////////////////////////
# ADD DATA MODULES
# ////////////////////////////////////////////////////////////////////////////////////////
from database.mental_mental import add_mentalsolo_data


class MainWindow(FramelessWindow, QtWidgets.QMainWindow, Ui_MainWindow):
    """
    The main window of the application.

    This class represents the main window of the application. It inherits from `FramelessWindow`,
    `QtWidgets.QMainWindow`, and `Ui_MainWindow`. It provides methods for handling various actions
    and events related to the main window.

    Attributes:
        mental_mental_model (QAbstractTableModel): The model for the mental mental table.
        ui (Ui_MainWindow): The user interface object for the main window.

    """

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.mental_mental_model = None
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        # Database init
        self.db_manager = DataManager()
        self.setup_models()
        # QSettings settings_manager setup
        self.settings = QSettings(tkc.ORGANIZATION_NAME, tkc.APPLICATION_NAME)
        self.window_controller = WindowController()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.restore_state()
        self.app_operations()
        self.slider_set_spinbox()
        self.stack_navigation()
        self.commits()
        self.delete_group()

    def switch_to_page1(self) -> None:
        """
        Switches to page 1 in the minderStacks widget and resizes the main window.

        This method sets the current widget of the minderStacks widget to the page widget,
        and resizes the main window to a width of 400 and a height of 111.

        Returns:
            None
        """
        self.minderStacks.setCurrentWidget(self.page)
        self.resize(160, 315)
        self.setMaximumSize(160, 315)
    
    def switch_to_page2(self) -> None:
        """
        Switches to page 2 in the minderStacks widget and resizes the main window.

        This method sets the current widget of the minderStacks widget to page_4,
        which represents page 2 in the user interface. It also resizes the main
        window to a width of 800 pixels and a height of 450 pixels.

        Returns:
            None
        """
        self.minderStacks.setCurrentWidget(self.page_4)
        self.setMaximumSize(800, 450)
        self.resize(800, 450)
    
    def handle_minimize_action(self) -> None:
        """
        Handles the minimize action of the main window.

        Toggles the minimize state of the window using the window controller.

        Raises:
            Exception: If an error occurs while minimizing the window.
        """
        try:
            self.window_controller.toggle_minimize(self)
        except Exception as e:
            logger.exception(f"Error occurred while minimizing {e}", exc_info=True)
    
    def handle_maximize_action(self) -> None:
        """
        Handles the maximize action of the window.

        Toggles the maximize state of the window using the window controller.
        If an error occurs, logs the exception with the error message.

        Raises:
            Exception: If an error occurs while maximizing the window.
        """
        try:
            self.window_controller.toggle_maximize(self)
        except Exception as e:
            logger.exception(f"Error occurred while maximizing {e}", exc_info=True)
    
    # ////////////////////////////////////////////////////////////////////////////////////////
    # APP-OPERATIONS setup
    # ////////////////////////////////////////////////////////////////////////////////////////
    def app_operations(self):
        """
        Performs the necessary operations for setting up the application.

        This method connects signals and slots, sets the initial state of the UI elements,
        and handles various actions triggered by the user.

        Raises:
            Exception: If an error occurs while setting up the app_operations.

        """
        try:
            self.minderStacks.currentChanged.connect(self.on_page_changed)
            last_index = self.settings.value("lastPageIndex", 0, type=int)
            self.minderStacks.setCurrentIndex(last_index)
            self.mental_mental_time.setTime(QTime.currentTime())
            self.mental_mental_date.setDate(QDate.currentDate())
            self.actionInput.triggered.connect(self.switch_to_page1)
            self.actionTableview.triggered.connect(self.switch_to_page2)
            self.actionMinimize.triggered.connect(self.handle_minimize_action)
            # self.minButton.clicked.connect(self.handle_minimize_action)
            # self.maxButton.clicked.connect(self.handle_maximize_action)
            self.actionMaximize.triggered.connect(self.handle_maximize_action)
        except Exception as e:
            logger.error(f"Error occurred while setting up app_operations : {e}", exc_info=True)
    
    def on_page_changed(self,
                        index):
        """
        Callback method triggered when the page is changed in the UI.

        Args:
            index (int): The index of the new page.

        Raises:
            Exception: If an error occurs while setting the last page index.

        """
        try:
            self.settings.setValue("lastPageIndex", index)
        except Exception as e:
            logger.error(f"{e}", exc_info=True)
    
    def commits(self):
        self.mental_mental_table_commit()
    
    # ////////////////////////////////////////////////////////////////////////////////////////
    # SLIDER UPDATES SPINBOX/VICE VERSA SETUP
    # ////////////////////////////////////////////////////////////////////////////////////////
    def slider_set_spinbox(self):
        """
        Connects sliders to their corresponding spinboxes.

        This method connects the following sliders to their corresponding spinboxes:
        - mood_slider to mood_spinbox
        - mania_slider to mania_spinbox
        - depression_slider to depression_spinbox
        - mixed_risk_slider to mixed_risk_spinbox

        Returns:
            None
        """
        connect_slider_to_spinbox = {
            self.mood_slider: self.mood,
            self.mania_slider: self.mania,
            self.depression_slider: self.depression,
            self.mixed_risk_slider: self.mixed_risk,
        }
        
        for slider, spinbox in connect_slider_to_spinbox.items():
            connect_slider_spinbox(slider, spinbox)
    
    # ////////////////////////////////////////////////////////////////////////////////////////
    # Minder Navigation
    # ////////////////////////////////////////////////////////////////////////////////////////
    def stack_navigation(self):
        """
        Connects the triggered signals of certain actions to change the stack pages.

        The method creates a dictionary `change_stack_pages` that maps actions to their corresponding page index.
        It then iterates over the dictionary and connects the `triggered` signal of each action to a lambda function
        that calls the `change_stack_page` method with the corresponding page index.

        Raises:
            Exception: If an error occurs during the connection of signals.

        """
        try:
            change_stack_pages = {
                self.actionInput: 0,
                self.actionTableview: 1,
            }
            
            for action, page in change_stack_pages.items():
                action.triggered.connect(lambda _, p=page: change_stack_page(self.minderStacks, p))

        except Exception as e:
            logger.error(f"An error has occurred: {e}", exc_info=True)
    
    def mental_mental_table_commit(self) -> None:
        """
        Connects the 'commit' action to the 'add_mentalsolo_data' function and inserts data into the mental_mental_table.

        Raises:
            Exception: If an error occurs during the process.
        """
        try:
            self.actionCommit.triggered.connect(
                lambda: add_mentalsolo_data(
                    self, {
                        "mental_mental_date": "mental_mental_date",
                        "mental_mental_time": "mental_mental_time",
                        "mood_slider": "mood_slider",
                        "mania_slider": "mania_slider",
                        "depression_slider": "depression_slider",
                        "mixed_risk_slider": "mixed_risk_slider",
                        "model": "mental_mental_model"
                    },
                    self.db_manager.insert_into_mental_mental_table, ))
        except Exception as e:
            logger.error(f"An Error has occurred {e}", exc_info=True)
    
    def delete_group(self):
        """
        Connects the delete action to the delete_selected_rows function.

        This method connects the delete action to the delete_selected_rows function,
        passing the necessary arguments to delete the selected rows in the mental_mental_table.

        Args:
            self: The instance of the main window.

        Returns:
            None
        """
        self.actionDelete.triggered.connect(
            lambda: delete_selected_rows(
                self,
                'mental_mental_table',
                'mental_mental_model'
            )
        )
    
    def setup_models(self) -> None:
        """
        Set up the models for the main window.

        This method creates and sets the mental_mental_model using the mental_mental_table.

        Returns:
            None
        """
        self.mental_mental_model = create_and_set_model(
            "mental_mental_table",
            self.mental_mental_table
        )
    
    def save_state(self):
        
        # save window geometry state
        try:
            self.settings.setValue("geometry", self.saveGeometry())
        except Exception as e:
            logger.error(f"Error saving the minds_module geo{e}", exc_info=True)
        try:
            self.settings.setValue("windowState", self.saveState())
        except Exception as e:
            logger.error(f"Error saving the minds_module geo{e}", exc_info=True)
    
    def restore_state(self) -> None:
        """
        Restores the window geometry and state.

        This method restores the previous geometry and state of the window
        by retrieving the values from the settings. If an error occurs during
        the restoration process, an error message is logged.

        Raises:
            Exception: If an error occurs while restoring the window geometry or state.
        """
        try:
            # restore window geometry state
            self.restoreGeometry(self.settings.value("geometry", QByteArray()))
        except Exception as e:
            logger.error(f"Error restoring the minds module : stress state {e}")
        
        try:
            self.restoreState(self.settings.value("windowState", QByteArray()))
        except Exception as e:
            logger.error(f"Error restoring WINDOW STATE {e}", exc_info=True)
    
    def closeEvent(self,
                   event: QCloseEvent) -> None:
        """
        Event handler for the close event of the window.

        Saves the state before closing the window.

        Args:
            event (QCloseEvent): The close event object.

        Returns:
            None
        """
        try:
            self.save_state()
        except Exception as e:
            logger.error(f"error saving state during closure: {e}", exc_info=True)
