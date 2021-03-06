import argparse  # from std


class BetterCalculator:
     @staticmethod
    def Conj(x, y):
        return #宇森

    @staticmethod
    def Pow(x, y):
        return #庭瑋

    @staticmethod
    def Gcd(x, y):
        return #咚咚組

    @staticmethod
    def Mod(x, y):
        return #學姊組



def main():

    # 準備參數解析
    example_text = "example usage: py.exe .\BetterCalculator.py 5 + c3"
    parser = argparse.ArgumentParser(
        description="簡單數學運算功能", epilog=example_text)
    parser.add_argument("x", help="第1個數字",
                        type=int)
    parser.add_argument("operator", help="運算符號:連接(c), 次方(p), 公約數(g), 餘數(m)",
                        type=str)
    parser.add_argument("y", help="第2個數字",
                        type=int)
    args = parser.parse_args()

    if(args.operator == "c"):
        ans = BetterCalculator.Add(args.x, args.y)
    elif(args.operator == "p"):
        ans = BetterCalculator.Multiple(args.x, args.y)
    elif(args.operator == "g"):
        ans = BetterCalculator.Minus(args.x, args.y)
    elif(args.operator == "m"):
        ans = BetterCalculator.Minus(args.x, args.y)
    else:
        ans = "輸入錯誤"

    # end
    if(ans == "輸入錯誤"):
        print(ans)
    else:
        print("結果:", args.x, "", args.operator, "", args.y, "=", ans)
        print()


if __name__ == "__main__":
    