# geometry
GEOMETRY = (1000, 600)
HELP_GEOMETRY = (500, 500)
SUCCEESS_SAVE_GEOMETRY = (500, 200)

# colors
TEXTBOX_COLOR = "#333333"
BORDER_TEXTBOX_COLOR = "#B2B2B2"
ANSWER_BACKGROUND_COLOR = "#191970"
ANSWER_TEXT_COLOR = "#F0E68C"
BUTTON_COLOR = "#4169E1"
BUTTON_HOVER_COLOR = "#4B0082"
SETTINGS_BG_COLOR = "#303030"
SETTINGS_SEGMENTED_BG_COLOR = "#4C4C4C"
SETTINGS_SELECTED_BUTTON_COLOR = "#191970"
BORDER_SETTINGS_COLOR = "#C0C0C0"
IMAGE_FRAME_COLOR = "#555555"

# fonts
NORMAL_FONT = "Quicksand Medium"
NORMAL_FONT_SIZE = 14
TTITLE_FONT = "Special Elite"
TTITLE_FONT_SIZE = 36
ANSWER_FONT = "URW Gothic"
ANSWER_FONT_SIZE = 20

# corner radius
CORNER_RADIUS = 20


# longer texts
PROMPT_EXPLANATION = 'Jesteś specjalistą w dziedzinie informatyki i właśnie otrzymałeś pytanie, na które musisz podać poprawną odpowiedź z podanych opcji.\nNapisz poprawną odpowiedź na to pytanie, wyjaśnij dlaczego wybrałeś tę opcję oraz opisz pozostałe pojęcia, które miałeś do wyboru, z odniesieniem do tematu pytania.\nFormat twojej wypowiedzi ma być podzielony na paragrafy z nagłówkami jako h2. Uwzględnij następujące nagłówki: "Poprawna odpowiedź", "Wyjaśnienie wybranej opcji", "Pozostałe odpowiedzi".\nPrzykład:\n"Poprawna odpowiedź\nOdpowiedź: C\nWyjaśnienie wybranej opcji\nWybrałem protokół SMTP, ponieważ służy on do wysyłania wiadomości e-mail od klientów na serwer poczty e-mail. Protokół ten działa na porcie 25 i może być również używany do przekazywania wiadomości e-mail ze źródłowego do docelowego serwera poczty e-mail. Protokół SMTP rzeczywiście służy do wysyłania wiadomości e-mail, jest więc poprawną odpowiedzią.\nPozostałe odpowiedzi\nOdpowiedź A - protokół POP3 jest używany przez klientów poczty e-mail do pobierania wiadomości z serwera poczty e-mail. Działa on na porcie 110. Protokól ten dotyczy więc poczty e-mail, ale ma przeciwne działanie niż wysyłanie e-maili, a mianowicie ich odbieranie.\nOdpowiedź B - DNS to protokół służący do tłumaczenia nazw domenowych (np. www.example.com) na adresy IP. Używa UDP do żądań i transferu informacji między serwerami DNS. W razie potrzeby do odpowiedzi DNS będzie używał TCP. DNS działa na porcie 53. Protokół DNS ma więc inne działanie niż wysyłanie wiadomości e-mail, nie może być to poprawna odpowiedź.\nOdpowiedź D - SSH służy do zdalnego zarządzania i bezpiecznego dostępu do zdalnych systemów. Udostępnia wiersz poleceń na komputerze zdalnym. Działa na porcie 22 i zapewnia silnie uwierzytelnianie i szyfrowany transport danych między klientem a komputerem zdalnym. Protokół SSH nie jest zatem związany z tematem pytania, gdyż posiada on zupełnie odmienne zastosowanie."\nUżywaj zwięzłego, konkretnego języka, który będzie łatwy do zrozumienia.\nTak wygląda pytanie:\n'


HELP_TEXT = """This program is used to help you solve problems from an IT theory exam (in Polish technical schools you need to pass two such examinations to get technician diploma) to speed up the preparation process. Here are step by step instructions: 
1) First you should paste an image of the question you are having trouble with (you should have your cursor inside the right widget) or import it from your disk. This image should be a screenshot of the IT exam theory question before clicking on the answer.
2) Then click the button 'get solution'. The program will communicate with AI and insert explanation to the textbox. That can take a while. After that you can edit this text according to your own preferences.
3) The last step is exporting this solution. You are able to this by clicking on 'Export' tab in settings in the bottom left corner. You can choose to create new file (which is required if you are exporting a solution for the first time) or extend a file previously created with this application. The only right extension is odt. 
While creating new file you should insert the proper directory and file name. And in the case of file extending you just need to choose the right file.
You don't have to export your solution of course. You can simply paste your next problem or go back to main menu by clicking on one of the buttons in 'Navigate' tab. """
