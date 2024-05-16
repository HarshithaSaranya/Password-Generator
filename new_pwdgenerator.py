import random
class Passwordgenerator:
    def __init__(self):
      self.length = length
      self.lowercase = "abcdefghijklmnopqrstuvwxyz"
      self.uppercase = self.lowercase.upper()
      self.digits ="1234567890"
      self.punctuations ="!@#$%^&*()"
    def generatepassword(self, length, uppercase_count, lowercase_count, punctuations_count,digits_count):
      if (uppercase_count + lowercase_count + punctuations_count + digits_count > length):
          print("password length cannot exceed length")
          return None
      char_pool = self.lowercase + self.uppercase + self.digits + self.punctuations
      password = [random.choice(self.lowercase) for _ in range(lowercase_count)]
      password += [random.choice(self.uppercase) for _ in range(uppercase_count)]
      password += [random.choice(self.punctuations) for _ in range(punctuations_count)]
      password += [random.choice(self.digits)for _ in range(digits_count)]

      password += [random.choice(char_pool) for _ in range(length-len(password))]
      random.shuffle(password)
      return "".join(password)
length = int(input("enter a length for password"))
uppercase_count = int(input("enter a number for uppercase"))
lowercase_count = int(input("enter a number for lowercase"))
digits_count = int(input("enter a number for digits"))
punctuations_count = int(input("enter a number for punctuations"))

pwd = Passwordgenerator()
password = pwd.generatepassword(length, uppercase_count, lowercase_count,digits_count, punctuations_count)


print("your generated password is",password)

