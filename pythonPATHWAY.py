#pythonPATHWAY
def score(): 
    diem_so = 0 
    Q1 = input('Câu 1: Sản phẩm nào sau đây không phải hãng điện thoại?\nA. Samsung\nB. Sony\nC. Gucci\nD. Apple\n Mời bạn chọn đáp án đúng: ').lower()
    if Q1 == 'c':
        diem_so += 1
        print('Điểm số của bạn đã tăng lên:', diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q2 = input('Câu 2: Ai là cầu thủ ghi nhiều bàn thắng nhất trong bóng đá?\nA. Lionel Messi\nB. Cristiano Ronaldo\nC. Pele\nD. Di stefano\n Mời bạn chọn đáp án đúng: ').lower()
    if Q2 == 'b':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q3 = input('Câu 3: Ai là tác giả của truyện ngắn "Truyện Kiều" ?\nA. Nguyễn Nhật Ánh\nB. Nguyễn Du\nC. Xuân Diệu\nD. Nam Cao\n Mời bạn chọn đáp án đúng: ').lower()
    if Q3 == 'b':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q4 = input('Câu 4: Thế văn hội Olympic tổ chức bao lâu một lần?\nA. 3\nB. 2\nC. 5\nD. 4\n Mời bạn chọn đáp án đúng: ').lower()
    if Q4 == 'd':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q5 = input('Câu 5: Ai trong số những ca sĩ sau đây là người Canada?\nA. Kanye West\nB. Justin Bieber\nC. Taylor Swift\nD. Ariana Grande\n Mời bạn chọn đáp án đúng: ').lower()
    if Q5 == 'b':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q6 = input('Câu 6: Ngôn ngữ lập trình nào được sử dụng rộng rãi nhất hiện nay?\nA. Pascal\nB. English\nC. Python\nD. French\n Mời bạn chọn đáp án đúng: ').lower()
    if Q6 == 'c':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q7 = input('Câu 7: Hãng xe nào sau đây không phải là siêu xe?\nA. Lamborghini\nB. McLaren\nC. Honda\nD. Ferrari\n Mời bạn chọn đáp án đúng: ').lower()
    if Q7 == 'c':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q8 = input('Câu 8: Tính tích phân ∫4x^2\nA. 4/3x^3\nB. 2x^2\nC. 4/5x^3\nD. 4x^3\n Mời bạn chọn đáp án đúng: ').lower()
    if Q8 == 'a':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q9 = input('Câu 9: 5C2 bằng bao nhiêu?\nA. 1\nB. 5\nC. 10\nD. 15\n Mời bạn chọn đáp án đúng: ').lower()
    if Q9 == 'c':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    Q10 = input('Câu 10: Màu nào sau đây không phải màu cơ bản(Primary color)?\nA. Đỏ\nB. Xanh dương\nC. Vàng\nD. Xanh lá\n Mời bạn chọn đáp án đúng: ').lower()
    if Q10 == 'd':
        diem_so += 1
        print("Điểm số của bạn đã tăng lên:" ,diem_so) 
    else:
        print("Điểm số của bạn vẫn là:", diem_so)
    return diem_so
score()
print("Cảm ơn bạn đã tham gia trò chơi")