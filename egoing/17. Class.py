
#* [클래스]
#! 아래의 코드는 아직 미완성이기 때문에 실행되지 않습니다.
#* 클래스는 객체를 표현하기 위한 문법, 객체를 만들어내기 위한 설계도
#* 그리고 맴버 변수와 메소드 들의 집합이라고 한다.
#* 클래스는 객체(Object)를 만들어 내기 위한 설계도이고, 객체(Object)는 클래스로 구현한 실체된 대상이다.

#* Class는 class 라는 키워드로 시작 된다.
#* class의 name은 Cal
#* c1, c2는 Object

class Cal(object):

c1 = Cal(10,10)         
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())