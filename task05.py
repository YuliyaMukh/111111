BAD_MARK = "you could better"

def get_feedback(mark):
    result = "Excellent"
    if mark <= 1:
        result = "very bad"
    elif 3 >= mark >= 2:
        result = "unsatisfactory"
    elif mark == 4:
        result = "satisfactory"
    elif 6 >= mark >= 5:
        result = "you could better"
    elif 8 >= mark >= 7:
        result = "good"
    return result

if __name__ == '__main__':
    assert get_feedback("10") == -1
    assert get_feedback(7.4) == -1
    assert get_feedback(True) == -1
    assert get_feedback(None) == -1
    assert get_feedback([1, 2, 3]) == -1
    assert get_feedback(20) == -1
    assert get_feedback(-20) == -1
    assert get_feedback(0) == "very bad"


