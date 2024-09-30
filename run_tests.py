import unittest
import pretty_errors

def run_all_tests():
    loader = unittest.TestLoader()

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(loader.discover('tests'))

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    run_all_tests()
