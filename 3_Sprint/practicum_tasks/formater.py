class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        self.text = text.lower()
        self.shift = shift
        self.is_encrypt = is_encrypt
        self.processed_text = []
        for i in range(len(self.text)):
            if self.text[i] in self.alphabet:
                if not self.is_encrypt:
                    number = (self.alphabet.find(self.text[i]) - self.shift) % len(self.alphabet)
                else:
                    number = (self.alphabet.find(self.text[i]) + self.shift) % len(self.alphabet)
                self.processed_text.append(self.alphabet[number])
            else:
                self.processed_text.append(self.text[i])
        return ''.join(self.processed_text)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 