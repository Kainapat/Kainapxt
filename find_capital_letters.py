# The Quick Brown Fox Jump Over The Lazy Dog
# The purpose of our Lives is to be Happy

def count_letters(text):
    # Count the number of letters in the text
    return len([char for char in text if char.isalpha()])

def count_vowels(text):
    # Count the number of vowels in the text
    vowels = 'aeiouAEIOU'
    return len([char for char in text if char in vowels])

def count_capitals(text):
    # Count the number of capital letters in the text and list them
    capitals = [char for char in text if char.isupper()]
    return len(capitals), ', '.join(capitals)

if __name__ == "__main__":
    input_text = input('Enter text: ')

    num_letters = count_letters(input_text)
    num_vowels = count_vowels(input_text)
    num_capitals, capital_list = count_capitals(input_text)

    print('Number of Letters:', num_letters)
    print('Number of Vowels:', num_vowels)
    print(f'Number of Capitals: {num_capitals}, [{capital_list}]')

'''

โปรแกรมดังกล่าวมีหน้าที่ในการนับอักขระและอักษรในข้อความที่ผู้ใช้ป้อนเข้ามา โดยมีการแยกหน้าที่และการอธิบายการทำงานดังนี้:

1. count_letters(text) เป็นฟังก์ชันที่ใช้ในการนับจำนวนอักขระทั้งหมดในข้อความที่รับมาผ่านพารามิเตอร์ text โดยใช้รายการคอมพรีเฮนชัน (list comprehension) 
และเงื่อนไข char.isalpha() เพื่อตรวจสอบว่าแต่ละอักขระเป็นอักษรหรือไม่ และคืนจำนวนอักขระทั้งหมดในข้อความนั้น

2. count_vowels(text) เป็นฟังก์ชันที่ใช้ในการนับจำนวนสระในข้อความที่รับมาผ่านพารามิเตอร์ text โดยใช้รายการคอมพรีเฮนชัน (list comprehension) 
และเงื่อนไข char in vowels เพื่อตรวจสอบว่าแต่ละอักขระเป็นสระหรือไม่ และคืนจำนวนสระทั้งหมดในข้อความนั้น

3. count_capitals(text) เป็นฟังก์ชันที่ใช้ในการนับจำนวนตัวอักษรใหญ่ (capital letters) และรายการของตัวอักษรใหญ่ในข้อความที่รับมาผ่านพารามิเตอร์ text 
โดยใช้รายการคอมพรีเฮนชัน (list comprehension) เพื่อเก็บตัวอักษรใหญ่ลงในรายการ capitals และคืนจำนวนตัวอักษรใหญ่ทั้งหมดและรายการของตัวอักษรใหญ่นั้น

4. ในบริบทหลัก (if __name__ == "__main__":) โปรแกรมจะรับข้อความจากผู้ใช้ผ่านฟังก์ชัน input() และจะเรียกใช้ฟังก์ชัน count_letters(), count_vowels(), 
และ count_capitals() เพื่อคำนวณและแสดงผลลัพธ์ในรูปแบบของจำนวนอักขระทั้งหมด จำนวนสระ และจำนวนตัวอักษรใหญ่ 
พร้อมกับรายการของตัวอักษรใหญ่ที่พบในข้อความนั้นในรูปแบบที่มีความชัดเจนและเรียบร้อย.

'''
