class User:
    def __init__(self, user_id, username):
      self.id = user_id #se auto crea la variable por eos puede ser el nombre que sea
      self.username = username
      self.followers = 0 #un atributo fijo 
      self.following = 0 
    
    def follow(self, user):
      user.followers += 1
      self.following += 1



 
user_1 = User("001", "angela") #manera de inicializar una clase con constructor adecuadoe
user_2 = User("002", "igna")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

