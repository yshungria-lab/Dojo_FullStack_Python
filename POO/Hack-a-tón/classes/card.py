class Card:

    def __init__( self , suit , point_val , string_val ):
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

    def comparar(self,otra_card):
        if self.point_val > otra_card.point_val:
            return True
        elif self.point_val < otra_card.point_val:
            return False
        else:
            if self.suit.value > otra_card.suit.value:
                return True
        return False