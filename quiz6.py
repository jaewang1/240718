# 문자 메세지 길이 판변 클래스. 문자 메세지 길이에 따라 문자 요금이 결정되는 프로그램
# 문자 메세지의 길이에 따라 부과되는 요금은, 클래스를 생성할 때 속성 정보로 갖게 된다.
# 요금이 부과될 문자 메세지의 길이를 정할 수 있도록 설정(속성 정보)
# 사용자로부터 문자 메세지를 입력 받아서 문자 요금을 반환하는 코드를 작성

class JW:
    def __init__(self, 길이, 요금, 요금2):
        self.jw_길이 = 길이
        self.jw_요금 = 요금
        self.jw_요금2 = 요금2

    def 문자(self,x):
        if len(x) >= self.jw_길이:
            print(self.jw_요금)
            result = self.jw_요금
        else:
            print(self.jw_요금2)
            result = self.jw_요금2
        return result

text=input('문자를 입력하세요:')

my_JW = JW( 20, 100,50)
my_JW.문자(text)






