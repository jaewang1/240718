# 게임 캐릭터 만들기, 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 갖는다.
# 기본 공격 함수를 갖는다. 기본 공격 함수는 사용시 "공격!" 문자열 화면에 출력.

class Game:
    def __init__(self, ID, SEX, JOB):
        self.game_ID = ID
        self.game_SEX = SEX
        self.game_JOB = JOB

    def att(self, aa, bb) :
        print(self.game_ID + "가 " + aa,",", bb + "을(를) 공격했다!")

print(Game("jw", "남", "학생"))
my_game = Game("jw", "남", "학생")
print(my_game)
my_game.att("괴물", "괴물2")

