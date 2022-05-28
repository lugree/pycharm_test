class TimeError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Time:
    def __init__(self, h, m, s):
        try:
            if h < 0 or h > 23:
                raise TimeError("Hour", h)
            if m < 0 or m > 59:
                raise TimeError("Minute", m)
            if s < 0 or s > 59:
                raise TimeError("Second", s)
        except TimeError as err:
            print(err)
        else:
            self.__hour = h
            self.__minute = m
            self.__second = s
            # finally:
        #    print("Object creation process")

    def __repr__(self):

        return "{:02d}:{:02d}:{}".format(self.__hour, self.__minute, self.__second)

    def get_second(self):
        return self.__second

    def get_hour(self):
        return self.__hour



    def get_minute(self):
        return self.__minute


    def set_hour(self, x):
        if x > 0 and x < 23:
            self.__hour = x
            print('Value successfuly changed')
        else:
            print("Sorry: Invalid value")


    def add_hour(self, h):

        if not isinstance(h, int):
            print('Please enter an integer')
        else:
            x = self.__hour + h
            self.__hour = x % 24

            return self.__hour


    def add_minute(self, m):
        x = self.__minute + m
        self.__minute = x % 60
        self.add_hour(x // 60)


    def add_second(self, s):
        x = self.__second + s
        self.__second = x % 60
        self.add_minute(x // 60)


# User
t = Time(3, 5, 48)
t1 = Time(5, 5, 5)
print(t)
t1.add_hour(2)
print(t)


# Programmer
class DateError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value



class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y)
            if m < 1 or m > 12:
                raise DateError("Month", m)
            if d < 1 or d > 30:
                raise DateError("Day", d)
        except DateError as err:
            print(err)
        else:
            self.__year = y
            self.__month = m
            self.__day = d

    def __str__(self):
        return "{}/{}/{}".format(self.__year, self.__month, self.__day)



    def add_year(self, y):
        self.__year += y

    def add_month(self, m):
        x = self.__month + m
        self.__month = ((x - 1) % 12) + 1


        self.add_year((x - 1) // 12)




    def add_day(self, d):
        x = self.__day + d
        while x > self.MONTH_DAYS[self.__month]:
            x = x - self.MONTH_DAYS[self.__month
            self.add_month(1)
        self.__day = x
        self.__day = x % 30
        if self.__day == 0:
            self.__day = 30
     
        self.add_month(x // 30)



class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)

    # def add_year(self, y):
    #    self.__date.add_year(y)
    #
    def add_month(self, m):
        self.__date.add_month(m)

    def add_day(self, d):
        self.__date.add_day(d)

    def add_minute(self, m):
        self.__time.add_minute(m)

    def add_second(self, s):
        self.__time.add_second(s)

    def add_hour(self, h):
        x = self.__time.get_hour() + h
        self.__time.add_hour(x % 24)
        self.__date.add_day(x // 24)


# d = Date(***)
# t = Time(***)
# dt = DateTime(d, t)

# #24.05
# class Person:
#     def __init__(self, fn, age):
#         self.full_name = fn
#         self.age = age
#         self.gender = None
#
#     def __str__(self):
#         print("Person")
#         if self.gender == "Female":
#             return "{} - {}".format(self.full_name, self.gender)
#         else:
#             return "{} - {}, {}".format(self.full_name, self.age, self.gender)
#
#
# class Student(Person):
#     def __init__(self, fn, a, univ, fac):
#         super().__init__(fn, a)
#         self.university = univ
#         self.faculty = fac
#
#     def __str__(self):
#         print("Student")
#         return "{}, faculty of {}\n".format(self.university, self.faculty) + super().__str__()
#
#
# s = Student("Julia Smith", 32, "YSU", "Informatics and Applied Mathematics")
# print(s)



