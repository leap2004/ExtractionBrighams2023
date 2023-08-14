class TextExtractor: 
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_resolution(self, text):
        pattern = r'(\d+x\d+)'
        resolution_values = re.findall(pattern, text)
        print("Resolution values", resolution_values)
        return resolution_values

    def extract_time(self, text):
        pattern = r'\b(\d{1,2}:\d{2}:\d{2})\b'
        time_values = re.findall(pattern, text)
        print("Time values", time_values)
        return time_values

    def extract_hosp(self, text):
        hosp_lines = []
        lines = text.split('\n')
        for line in lines:
            if 'hospital' in line.lower():
                hosp_lines.append(line)
        return hosp_lines

    def extract_most_likely_name(self, text):
        names = []
        doc = self.nlp(text)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                names.append(ent.text)

        if not names:
            return None

        most_common_name = Counter(names).most_common(1)[0][0]
        return most_common_name

    def extract_seq(self, text):
        pattern = r'(?i)\bSeq\s+(\d+)\b'
        values = re.findall(pattern, text)
        print("Seq values", values)
        return values

    def extract_filt(self, text):
        pattern = r'(?i)\bFilt\.\s+(\d+)\b'
        filt_values = re.findall(pattern, text)
        print('filt values,', filt_values)
        return filt_values

    def extract_mask(self, text):
        pattern = r'(?i)\bMASK\s*=\s*(\d+)\b'
        mask_values = re.findall(pattern, text)
        print("Mask values", mask_values)
        return mask_values

    def extract_CRA(self, text):
        pattern = r'(?i)\bCRA\s+(\d+)\b'
        CRA_values = re.findall(pattern, text)
        print("CRA values", CRA_values)
        return CRA_values

    def extract_L(self, text):
        pattern = r'(?i)\bLi-\s*(\d+\.\d+)\s*deg\b'
        l_values = re.findall(pattern, text)
        print("L values", l_values)
        return l_values

    def extract_tilt(self, text):
        pattern = r'(?i)\bTilt\s+(\d+)\b'
        tilt_values = re.findall(pattern, text)
        print("Tile values", tilt_values)
        return tilt_values

    def extract_dates(self, text):
        date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
        dates = re.findall(date_pattern, text)
        return dates

    def extract_values(self, text, term):
        pattern = fr'(?i)(\b{term}:\s*|\b{term}\s* = )\s*(.*)'
        values = re.findall(pattern, text)
        return values
