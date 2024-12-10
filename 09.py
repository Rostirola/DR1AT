class UserProfile:
    def __init__(self, username, name, email, age):
        self.username = username
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"UserProfile(username='{self.username}', name='{self.name}', email='{self.email}', age={self.age})"


class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, user_profile):
        index = self._hash(user_profile.username)
        # Verifica se o usuário já existe e atualiza
        for profile in self.table[index]:
            if profile.username == user_profile.username:
                profile.name = user_profile.name
                profile.email = user_profile.email
                profile.age = user_profile.age
                return
        # Caso contrário, adiciona novo perfil
        self.table[index].append(user_profile)

    def retrieve(self, username):
        index = self._hash(username)
        for profile in self.table[index]:
            if profile.username == username:
                return profile
        return None

    def remove(self, username):
        index = self._hash(username)
        for i, profile in enumerate(self.table[index]):
            if profile.username == username:
                del self.table[index][i]
                return True
        return False


# Exemplo de uso
if __name__ == "__main__":
    ht = HashTable()

    # Inserindo perfis de usuários
    ht.insert(UserProfile("juan123", "Juan Silva", "juan@example.com", 30))
    ht.insert(UserProfile("maria456", "Maria Souza", "maria@example.com", 25))
    ht.insert(UserProfile("pedro789", "Pedro Santos", "pedro@example.com", 28))

    # Recuperando um perfil
    usuario = ht.retrieve("maria456")
    print(usuario)  # Output: UserProfile(username='maria456', name='Maria Souza', email='maria@example.com', age=25)

    # Removendo um perfil
    removido = ht.remove("pedro789")
    print(removido)  # Output: True

    # Tentar recuperar um perfil removido
    usuario = ht.retrieve("pedro789")
    print(usuario)  # Output: None
