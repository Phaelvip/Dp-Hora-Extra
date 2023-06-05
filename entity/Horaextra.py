class DpHoraExtraTolera:
    def __init__(self, id, nome, codigo, data, aut, hr_atual, hr_solicit, tolera):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.data = data
        self.aut = aut
        self.hr_atual = hr_atual
        self.hr_solicit = hr_solicit
        self.tolera = tolera
        self.tolera_inicio = self.calculate_tolera_inicio()
        self.tolera_fim = self.calculate_tolera_fim()

    def calculate_tolera_inicio(self):
        return self.hr_solicit - self.tolera

    def calculate_tolera_fim(self):
        tolera_secs = self.time_to_seconds(self.tolera)
        hr_solicit_secs = self.time_to_seconds(self.hr_solicit)
        tolera_fim_secs = hr_solicit_secs + tolera_secs
        return self.seconds_to_time(tolera_fim_secs)

    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds

    @staticmethod
    def seconds_to_time(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"