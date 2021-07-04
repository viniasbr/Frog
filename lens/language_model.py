from gi.repository import Gtk


class LanguageModel(Gtk.ListStore):
    def __init__(self):
        super(LanguageModel, self).__init__(str, str)

        self.append(["afr", "Afrikaans"])
        self.append(["amh", "Amharic"])
        self.append(["ara", "Arabic"])
        self.append(["asm", "Assamese"])
        self.append(["aze", "Azerbaijani"])
        self.append(["aze_cyrl", "Azerbaijani - Cyrilic"])
        self.append(["bel", "Belarusian"])
        self.append(["ben", "Bengali"])
        self.append(["bod", "Tibetan"])
        self.append(["bos", "Bosnian"])
        self.append(["bre", "Breton"])
        self.append(["bul", "Bulgarian"])
        self.append(["cat", "Catalan; Valencian"])
        self.append(["ceb", "Cebuano"])
        self.append(["ces", "Czech"])
        self.append(["chi_sim", "Chinese - Simplified"])
        self.append(["chi_tra", "Chinese - Traditional"])
        self.append(["chr", "Cherokee"])
        self.append(["cos", "Corsican"])
        self.append(["cym", "Welsh"])
        self.append(["dan", "Danish"])
        self.append(["deu", "German"])
        self.append(["dzo", "Dzongkha"])
        self.append(["ell", "Greek, Modern (1453-)"])
        self.append(["eng", "English"])
        self.append(["enm", "English, Middle (1100-1500)"])
        self.append(["epo", "Esperanto"])
        self.append(["equ", "Math / equation detection module"])
        self.append(["est", "Estonian"])
        self.append(["eus", "Basque"])
        self.append(["fao", "Faroese"])
        self.append(["fas", "Persian"])
        self.append(["fil", "Filipino (old - Tagalog)"])
        self.append(["fin", "Finnish"])
        self.append(["fra", "French"])
        self.append(["frk", "German - Fraktur"])
        self.append(["frm", "French, Middle (ca.1400-1600)"])
        self.append(["fry", "Western Frisian"])
        self.append(["gla", "Scottish Gaelic"])
        self.append(["gle", "Irish"])
        self.append(["glg", "Galician"])
        self.append(["grc", "Greek, Ancient (to 1453) (contrib)"])
        self.append(["guj", "Gujarati"])
        self.append(["hat", "Haitian; Haitian Creole"])
        self.append(["heb", "Hebrew"])
        self.append(["hin", "Hindi"])
        self.append(["hrv", "Croatian"])
        self.append(["hun", "Hungarian"])
        self.append(["hye", "Armenian"])
        self.append(["iku", "Inuktitut"])
        self.append(["ind", "Indonesian"])
        self.append(["isl", "Icelandic"])
        self.append(["ita", "Italian"])
        self.append(["ita_old", "Italian - Old"])
        self.append(["jav", "Javanese"])
        self.append(["jpn", "Japanese"])
        self.append(["kan", "Kannada"])
        self.append(["kat", "Georgian"])
        self.append(["kat_old", "Georgian - Old"])
        self.append(["kaz", "Kazakh"])
        self.append(["khm", "Central Khmer"])
        self.append(["kir", "Kirghiz; Kyrgyz"])
        self.append(["kmr", "Kurmanji (Kurdish - Latin Script)"])
        self.append(["kor", "Korean"])
        self.append(["kor_vert", "Korean (vertical)"])
        self.append(["lao", "Lao"])
        self.append(["lat", "Latin"])
        self.append(["lav", "Latvian"])
        self.append(["lit", "Lithuanian"])
        self.append(["ltz", "Luxembourgish"])
        self.append(["mal", "Malayalam"])
        self.append(["mar", "Marathi"])
        self.append(["mkd", "Macedonian"])
        self.append(["mlt", "Maltese"])
        self.append(["mon", "Mongolian"])
        self.append(["mri", "Maori"])
        self.append(["msa", "Malay"])
        self.append(["mya", "Burmese"])
        self.append(["nep", "Nepali"])
        self.append(["nld", "Dutch; Flemish"])
        self.append(["nor", "Norwegian"])
        self.append(["oci", "Occitan (post 1500)"])
        self.append(["ori", "Oriya"])
        self.append(["osd", "Orientation and script detection module"])
        self.append(["pan", "Panjabi; Punjabi"])
        self.append(["pol", "Polish"])
        self.append(["por", "Portuguese"])
        self.append(["pus", "Pushto; Pashto"])
        self.append(["que", "Quechua"])
        self.append(["ron", "Romanian; Moldavian; Moldovan"])
        self.append(["rus", "Russian"])
        self.append(["san", "Sanskrit"])
        self.append(["sin", "Sinhala; Sinhalese"])
        self.append(["slk", "Slovak"])
        self.append(["slv", "Slovenian"])
        self.append(["snd", "Sindhi"])
        self.append(["spa", "Spanish; Castilian"])
        self.append(["spa_old", "Spanish; Castilian - Old"])
        self.append(["sqi", "Albanian"])
        self.append(["srp", "Serbian"])
        self.append(["srp_latn", "Serbian - Latin"])
        self.append(["sun", "Sundanese"])
        self.append(["swa", "Swahili"])
        self.append(["swe", "Swedish"])
        self.append(["syr", "Syriac"])
        self.append(["tam", "Tamil"])
        self.append(["tat", "Tatar"])
        self.append(["tel", "Telugu"])
        self.append(["tgk", "Tajik"])
        self.append(["tha", "Thai"])
        self.append(["tir", "Tigrinya"])
        self.append(["ton", "Tonga"])
        self.append(["tur", "Turkish"])
        self.append(["uig", "Uighur; Uyghur"])
        self.append(["ukr", "Ukrainian"])
        self.append(["urd", "Urdu"])
        self.append(["uzb", "Uzbek"])
        self.append(["uzb_cyrl", "Uzbek - Cyrilic"])
        self.append(["vie", "Vietnamese"])
        self.append(["yid", "Yiddish"])
        self.append(["yor", "Yoruba"])
