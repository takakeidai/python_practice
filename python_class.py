

# # クラス変数とクラスメソッド

# クラス1

class Circle():
    pi = 3.14 # πはcircle(円)が持つべき情報だから、Circleクラスの中に入れる情報だが、
                #個別のcircleが共通して持つべきもの、ここのインスタンスで変わるものではないからクラス変数として定義しておく。

    def __init__(self, radius):
        self.radius = radius

    #　クラスメソッド：
    # @classmethod
    # def show_pi(cls):
    #     return cls.pi
    @classmethod
    def show_pi(cls):
        return Circle.pi # これでもできちゃうのは何故か？　<= ① 先生に聞く

    def calculate_circle_are(self):
        area = self.radius * self.radius * Circle.pi #このように Circle.__piは内側では呼び出せるが、その側ではこのような操作はできない。
        return area
    
# circle_1 = Circle(10)

# print(circle_1.show_pi())

# print(circle_1.calculate_circle_are())

# # クラス変数は、個別のインスタンスが持つ性質の1つであるから以下のようにもアクセスできる。しかし、__がついている場合外側からはアクセスできない。
# print(circle_1.pi)

# # クラス変数は、クラス.変数でもアクセス可能。ただし、__がついている場合を除く。
# print(Circle.pi)


## より具体的にインスタンス変数、クラス変数、パブリック、プライベートの枠組みで変数を見ると
## (パブリック)インスタンス変数/プライベートインスタンス変数/(パ)ブリック)クラス変数/プライベートクラス変数

## より具体的にインスタンスメソッド、クラスメソッド、パブリックメソッド、プライベートメッドの枠組みでメソッドを見ると
## (パブリック)インスタンスメソッド/プライベートインスタンスメソッド/(パブリック)クラスメソッド/プライベートクラスメソッド

# print('#####################################################################################################################')

# クラス2

class Car():

    counter = 0

    speed_limit = 170
    side_of_handle = 'right'
    __id_given_by_consumer_affairs_agency = 6

    def __init__(self, name, body_type, max_speed, price):
        # (パブリック)インスタンス変数
        self.name = name
        self.body_type = body_type
        self.max_speed = max_speed
        self.price = price
        Car.counter += 1
        self.id = Car.counter
        #　プライベートインスタンス変数。__をつけることで外からアクセスできないようにする。
        self.__secret_number_for_car = 88

    def resale_value(self):
        resale_value = self.price * 0.2
        return resale_value
        

    def calculate_repair_cost(self):

        #　関数の中でもインスタンス変数を定義できる。
        #　ここでは全ての車の修理費用は300000円と仮定し、
        self.repair_cost = 300000
        repair = self.repair_cost*1.1
        return repair

    def __private_instance_method(self):
        print('this is private instance method')
    
    @classmethod
    def f(cls):
        legal_speed = 100
        speed_over_1 = cls.speed_limit - legal_speed
        speed_over_2 = Car.speed_limit - legal_speed
        cls.color = 'black'
        print(speed_over_1, speed_over_2, cls.color)

        # ちなみにクラスメソッド内ではselfとついたインスタンス変数を使えない。よって、引数として渡してあげるかするしかない。

    @classmethod
    def __private_class_method(cls):
        print('this is private class method')


# print('# インスタンスに関わる諸々')

# prius = Car('prius', 'sedan','200', 3000000)

# print(prius.name, prius.body_type,prius.max_speed,prius.price)
# # print(prius.__secret_number_for_car)                                 #　当然外からは呼び出せない

# print(Car.counter, prius.counter, prius.id)

# aqua = Car('aqua', 'sedan','220', 3400000)

# print(Car.counter, prius.id, aqua.id)

# print(prius.resale_value())
# # print(prius.repair_cost)                                              #　メソッド内で定義したインスタンス変数は参照できない
# print(prius.calculate_repair_cost())
# # print(prius.__private_instance_method)                                 #　当然外からは呼び出せない


# print('#　クラスに関わる諸々')

# print(Car.speed_limit)
# print(Car.side_of_handle)
# # print(Car.__id_given_by_consumer_affairs_agency)                      #　当然外からは呼び出せない
# # print(Car.color)                                                      #　メソッド内で定義したクラス変数は参照できない

# print(Car.f())
# # print(Car.__private_class_method())                                   #　当然外からは呼び出せない

# print('#####################################################################################################################')


# static method

#　スタティックメソッドとは、クラスメソッドとほぼ同じ構文で@staticmethodをつけることで作成できる。
#　スタティックメソッドの定義では引数にclsやselfは渡されず、呼び出し時に渡した値がそのままメソッドに渡される
#　スタティックメソッドは、クラスに属すがそのクラスに依存しないメソッド
#　クラスのメンバにはアクセスできない
#　実行するには、クラス名.スタティックメソッド名、これによりインスタンスを生成しなくてもメソッドが呼び出せる
#　スタティックメソッドの定義文内では、インスタンス変数、クラス変数、他の関数にはアクセスできない。


class Circle():
    pi = 3.14 # πはcircle(円)が持つべき情報だから、Circleクラスの中に入れる情報だが、
                #個別のcircleが共通して持つべきもの、ここのインスタンスで変わるものではないからクラス変数として定義しておく。

    def __init__(self, radius):
        self.radius = radius

    #　クラスメソッド：
    # @classmethod
    # def show_pi(cls):
    #     return cls.pi
    @classmethod
    def show_pi(cls):
        return Circle.pi # これでもできちゃうのは何故か？　<= ① 先生に聞く

    def calculate_circle_are(self):
        area = self.radius * self.radius * Circle.pi #このように Circle.__piは内側では呼び出せるが、その側ではこのような操作はできない。
        return area
    
    # インスタンスともクラスとも全く関係ない処理
    @staticmethod
    def only_add(x, y):
        return x + y

    @staticmethod
    def only_this():
        return "only_this"


    #　引数にインスタンスが渡されないといけない処理
    @staticmethod
    def compare_circle_are(circle1, circle2):
        ratio = circle1.calculate_circle_are()/circle2.calculate_circle_are()
        return ratio

    #　クラスのオブジェクト自体を入れて行われる処理
    @staticmethod
    def dubble_pi(circle):
        return circle.pi * 2



# static_method_1 = Circle.only_add(1,2)
# print(static_method_1)

# print(Circle.only_this())


# circle_1 = Circle(14)
# circle_2 = Circle(3)
# static_method_2 = Circle.compare_circle_are(circle_1, circle_2)
# print(static_method_2)

# # Circle.piが成り立ってしまうから、Circleというオブジェクト自体を入れてもメソッドが正常に処理される。
# static_method_3 = Circle.dubble_pi(Circle)
# print(static_method_3)



#　「Python実践　入門」 p.139　スタティックメソッド

class Page():
    def __init__(self, num, content):
        self.num = num
        self.content = content


    @staticmethod
    def dubble(x):
        return x*2
    

    @staticmethod
    def check_blank(page):
        return bool(page.content)


# # page = 'yeah'
# # print(Page.check_blank(page))   # page.contentが定義されないと出力される

# page = Page(1, '')
# print(Page.check_blank(page))
# print(Page.dubble(3))              # 6と出力される
