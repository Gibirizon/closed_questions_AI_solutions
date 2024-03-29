import customtkinter as ctk
from settings import *


class Settings(ctk.CTkTabview):
    def __init__(self, parent, *args):
        super().__init__(
            master=parent,
            fg_color=SETTINGS_BG_COLOR,
            segmented_button_fg_color=SETTINGS_SEGMENTED_BG_COLOR,
            segmented_button_selected_color=SETTINGS_SELECTED_BUTTON_COLOR,
            segmented_button_unselected_color=SETTINGS_SEGMENTED_BG_COLOR,
            segmented_button_selected_hover_color=BUTTON_HOVER_COLOR,
            segmented_button_unselected_hover_color=BUTTON_HOVER_COLOR,
        )

        # buttons
        self.add("Navigate")
        self.add("Help")

        SettingsButtons(
            self.tab("Navigate"),
            "Back to main menu",
            args[0],
        ).pack(expand=True)
        SettingsButtons(
            self.tab("Help"),
            "Help",
            args[1],
        ).pack(expand=True)

        self.place(rely=0.65, relx=0, relheight=0.35, relwidth=1)


class SettingsButtons(ctk.CTkButton):
    def __init__(self, parent, text, func=None):
        super().__init__(
            master=parent,
            text=text,
            command=func,
            font=ctk.CTkFont(family=NORMAL_FONT, size=NORMAL_FONT_SIZE),
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
        )


class CommonLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(
            master=parent,
            text=text,
            font=ctk.CTkFont(family=NORMAL_FONT, size=NORMAL_FONT_SIZE),
        )


class SettingsEntry(ctk.CTkEntry):
    def __init__(self, parent, textvariable):
        super().__init__(
            master=parent,
            textvariable=textvariable,
            font=ctk.CTkFont(family=NORMAL_FONT, size=NORMAL_FONT_SIZE),
        )

        self.pack(expand=True, fill="x", padx=10, pady=5)


class ExtendFile(ctk.CTkFrame):
    def __init__(self, parent, path_string, export_func):
        super().__init__(master=parent, fg_color=SETTINGS_SEGMENTED_BG_COLOR)
        self.path_string = path_string
        SettingsButtons(self, "Open file search", self.open_file_dialog).pack(
            expand=True, pady=5
        )
        SettingsEntry(self, self.path_string)
        SettingsButtons(
            self, "Save solution to a file", lambda: export_func(self.path_string.get())
        ).pack(expand=True, pady=5)

        self.pack(expand=True, fill="both")

    def open_file_dialog(self):
        path = ctk.filedialog.askopenfilename(
            filetypes=(("text files", "*.odt"), ("text files", "*.docx")),
            title="Choose file to extend",
            initialdir="/home",
        )
        self.path_string.set(path)


class NewFilePath(ctk.CTkFrame):
    def __init__(self, parent, path_string):
        super().__init__(master=parent, fg_color=SETTINGS_SEGMENTED_BG_COLOR)
        self.path_string = path_string
        SettingsButtons(self, "Open directory search", self.open_dir_dialog).pack(
            pady=5, expand=True
        )
        SettingsEntry(self, self.path_string)

        self.pack(side="left", expand=True, fill="both", padx=10, pady=5)

    def open_dir_dialog(self):
        path = ctk.filedialog.askdirectory(
            title="Choose directory to create file",
            initialdir="/home",
        )
        self.path_string.set(path)


class FileName(ctk.CTkFrame):
    def __init__(self, parent, file_name_string, font):
        super().__init__(master=parent, fg_color=SETTINGS_SEGMENTED_BG_COLOR)
        self.file_name = file_name_string
        CommonLabel(self, "Enter new file name:").pack(pady=5, expand=True)
        SettingsEntry(self, self.file_name)

        self.pack(side="left", expand=True, fill="both", padx=10, pady=5)


class SuccessSave(ctk.CTkToplevel):
    def __init__(self, parent, font):
        super().__init__(master=parent)
        width = SUCCEESS_SAVE_GEOMETRY[0]
        height = SUCCEESS_SAVE_GEOMETRY[1]
        half_width = int((self.winfo_screenwidth() / 2) - (width / 2))
        half_height = int((self.winfo_screenheight() / 2) - (height / 2))

        self.geometry(f"{width}x{height}+{half_width}+{half_height}")
        self.minsize(width, height)
        self.title("Success")

        self.success_label = CommonLabel(self, "Successfully saved file")
        self.success_label.configure(font=font)
        self.success_label.pack(expand=True, fill="both")
