class ScanConfig:

    START_MESSAGE_BOX_TITLE: str = "Folder not added!!!"
    START_MESSAGE_BOX_TEXT: str = (
        "Please select a folder or duplicate search will not be possible."
    )
    START_STATUSBAR_INFO_MESSAGE: str = "Scanning started."
    ON_FINISHED_STATUSBAR_SUCCESS_MESSAGE: str = (
        "Scan completed, results loaded into table."
    )
    ON_FINISHED_STATUSBAR_SUCCESS_MESSAGE_NOT_FILE: str = (
        "You do not have a duplicate file."
    )

    CRITICAL_START: str = "Scan-start"
    CRITICAL_CLEAR_TABLE: str = "Scan-clear_table"
    CRITICAL_ON_FINISHED: str = "Scan-__on_finished"

    INFO_STATUSBAR_TIME_OUT: int = 3
    ERROR_STATUSBAR_TIME_OUT: int = 5
    WARNING_STATUSBAR_TIME_OUT: int = 5
    SUCCESS_STATUSBAR_TIME_OUT: int = 10


class FolderPathConfig:

    ADD_FILE_DIOLOG_CAPTION: str = "Select search index"
    ADD_MESSAGE_BOX_TITLE: str = "Folder already added!!!"
    ADD_MESSAGE_BOX_TEXT: str = "You cannot add the same folder more than once."
    REMOVE_WARNING_STATUSBAR_MESSAGE: str = (
        "Please select an element to delete from the list of paths to scan."
    )
    RESET_SUCCESS_STATUSBAR_MESSAGE: str = "The list of paths to scan has been reset."

    CRITICAL_ADD: str = "FolderPath-add"
    CRITICAL_REMOVE: str = "FolderPath-remove"

    INFO_STATUSBAR_TIME_OUT: int = 3
    ERROR_STATUSBAR_TIME_OUT: int = 5
    WARNING_STATUSBAR_TIME_OUT: int = 5
    SUCCESS_STATUSBAR_TIME_OUT: int = 10


class DeleteOptionsConfig:

    DELETE_MESSAGE_BOX_TITLE: str = "No scanning done!!!"
    DELETE_MESSAGE_BOX_TEXT: str = "Please scan and try again."
    DELETE_INFO_STATUSBAR_MESSAGE: str = "Deletion process started."

    SELECT_TIME_WARNING_STATUSBAR_MESSAGE_NOT_SCAN: str = (
        "Scan not performed, no data, please scan"
    )
    SELECT_TIME_WARNING_STATUSBAR_MESSAGE_NOT_COPY: str = (
        "There is no duplicate file, you cannot select"
    )
    SELECT_TIME_WARNING_STATUSBAR_MESSAGE_SELECT: str = (
        "TThe elections have already been made, you cannot make the same choice again."
    )
    FINISHED_WARNING_STATUSBAR_MESSAGE: str = "No files could be deleted"
    FINISHED_ERROR_STATUSBAR_MESSAGE_UNDELETABLE_FILE: str = (
        "An error occurred while deleting some files"
    )
    FINISHED_SUCCESS_STATUSBAR_MESSAGE_ALL: str = "All copies deleted."
    FINISHED_SUCCESS_STATUSBAR_MESSAGE_SELECTED: str = "All selected copies are deleted"

    CRITICAL_DELETE: str = "DeleteOptions-delete"
    CRITICAL_SELECT_TIME: str = "DeleteOptions-select_time"
    CRITICAL_FINISHED: str = "DeleteOptions-__finished"

    INFO_STATUSBAR_TIME_OUT: int = 3
    ERROR_STATUSBAR_TIME_OUT: int = 5
    WARNING_STATUSBAR_TIME_OUT: int = 5
    SUCCESS_STATUSBAR_TIME_OUT: int = 10
