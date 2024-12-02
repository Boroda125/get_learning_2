import traceback


class Calcylator:
    last_rez = None

    def sum(self, n1, n2):
        self.last_rez = n1 + n2
        return self.last_rez

    def divizion(self, n1, n2):
        try:
            rez = n1 / n2
            self.last_rez = rez
            return rez
        except:
          traceback.print_exc()


    def print_last_rez (self):
        print(self.last_rez)