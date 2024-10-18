print("Простые Юнит-Тесты")
import unittest
#import runner
#import rt_with_exceptions

import rt_with_exceptions as runner
import logging



class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="utf-8")

    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk (self):

        walk_man = runner.Runner("Johnny First", -5 ) # ловим ошибку в логах

        for  _ in range ( 10):
            walk_man.walk()

        self.assertEqual(walk_man.distance, 50)
        #print("Ходьба", walk_man.distance , self.assertEqual (walk_man.distance , 50 ))
        logging.warning(f" {walk_man.name} выполнен успешно")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run (self):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding="utf-8")


        run_man = runner.Runner ( "Bille Secon", 3)


        for _  in range (10):
            run_man.run()

        self.assertEqual(run_man.distance, 60)
        print("Бег ",  run_man.distance ,  self.assertEqual ( run_man.distance , 60 ) )

        logging.warning(f" {run_man.name} выполнен успешно")

if __name__ == '__main__':

    #logging.basicConfig (level = logging.INFO, filemode = 'w', filename = 'runner_tests.log', encoding="utf-8")

    unittest.main()

