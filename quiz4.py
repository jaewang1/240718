# 부동산 정보 입력 클래스 부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 지어진 년도
# 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력

class JW:
    def __init__(self, a, b, c, d, e):
        self.jw_a = a
        self.jw_b = b
        self.jw_c = c
        self.jw_d = d
        self.jw_e = e
    def print_info(self):
        print("건물 위치: ", self.jw_a,
              "\n건물 평수: ", self.jw_b,
              "\n건물 종류: ", self.jw_c,
              "\n건물 가격: ", self.jw_d,
              "\n건물 년도:", self.jw_e )


print(JW("경기도", "28평", "아파트", "5억", "2020년"))
my_JW = JW("경기도", "28평", "아파트", "5억", "2020년")
my_JW.print_info()


