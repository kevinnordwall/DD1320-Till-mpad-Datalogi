import unittest
import syntax_test as s

class Testsyntax(unittest.TestCase):
    ''' Testar Sample input/output 1 '''
    def test_case1(self):
        std_in = []
        with open("correct_sample.in") as corr:
            for row in corr:
                row = row.strip()
                if row == "#":
                    break
                std_in.append(row)

        std_out = []
        with open("correct_sample.ans") as corr_ans:
            for row in corr_ans:
                row = row.strip()
                std_out.append(row)

        for i, j in enumerate(std_out):
            self.assertEqual(s.main(std_in[i]), j)


    ''' Testar Sample input/output 2 '''
    def test_case2(self):
        std_in = []
        with open("incorrect_sample.in") as incorr:
            for row in incorr:
                row = row.strip("\n")
                if row == "#":
                    break
                std_in.append(row)

        std_out = []
        with open("incorrect_sample.ans") as incorr_ans:
            for row in incorr_ans:
                row = row.strip("\n")
                std_out.append(row)

        for i, j in enumerate(std_out):
            self.assertEqual(s.main(std_in[i]), j)

if __name__ == '__main__':
    unittest.main()