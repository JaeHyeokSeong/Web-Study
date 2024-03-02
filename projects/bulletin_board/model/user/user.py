
class User:

    def __init__(self, email, password, name=None, t='u'):
        self.email = email
        self.password = password
        self.name = name
        self.t = t # 고객 타입 - u: 일반 사용자, a: 관리자

    def update_email(self):
        pass

    def update_password(self):
        pass

    def update_name(self):
        pass

    def update_t(self):
        pass

    def login(self):
        pass
     
