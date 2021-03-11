"""Hàm any() trả về:

True nếu có ít nhất 1 phần tử trong iterable là True.
False nếu tất cả các phần tử trong iterable là False hoặc iterable rỗng."""

s = 'qA2'
#str.isalnum() : phuong phap kiem tra tat ca cac ki tu trong chuoi co thuot loai (a-z , A-Z , 0-9) hay khong ?
print(any(x.isalnum() for x in s))
#str.isalpha() : phuong phap kiem tra tat ca ki tu co cung loai chu hay khong  (a-z , A-Z)
print(any(x.isalpha() for x in s))
#str.isdigit() : phuong phap kiem tra tat ca ki tu co thuoc kieu so hay khong (0-9)
print(any(x.isdigit() for x in s))
#str.islower() : phuong phap kiem tra tat ca ki tu tra ve dung neu tat ca chu so deu la chu thuong thi tra ve True , con lai thi False (a-z)
print(any(x.islower() for x in s))
#str.isupper() : phuong phap kiem tra tat ca ki tu tra ve dung neu tat ca chu so deu la chu in hoa thi tra ve True , con lai thi False (A-Z)
print(any(x.isupper() for x in s))
