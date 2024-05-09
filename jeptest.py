import unittest
from tkinter import Tk
from jeopardy_game import JeopardyGame  
class TestJeopardyGame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = JeopardyGame(self.root)

    def test_initialization(self):
        self.assertEqual(self.app.current_player, "User")
        self.assertEqual(self.app.fake_player, "Computer")
        self.assertEqual(self.app.fake_player_points, 0)
        self.assertEqual(self.app.user_points, 0)
        self.assertEqual(self.app.category_var.get(), "Python")
        self.assertEqual(self.app.question_var.get(), "")

    @patch('tkinter.messagebox.askyesno')
    @patch('tkinter.simpledialog.askstring')
    
    def test_pick_question(self, mock_askstring, mock_askyesno):
        mock_askyesno.return_value = True
        mock_askstring.return_value = "Data structure"

        self.app.pick_question()
        self.assertEqual(self.app.current_player, "User")
        self.assertEqual(self.app.user_points, 100)

        mock_askyesno.return_value = False
        self.app.pick_question()
        self.assertEqual(self.app.current_player, "User")
        self.assertEqual(self.app.user_points, 100)

    @patch('tkinter.messagebox.askyesno')
    @patch('tkinter.simpledialog.askstring')
    def test_fake_player_answer(self, mock_askstring, mock_askyesno):
        mock_askyesno.return_value = False
        mock_askstring.return_value = None  # Fake player does not input any answer

        with patch.object(self.app, 'fake_player_points_label') as fake_player_points_label_mock:
            self.app.pick_question()
            self.assertEqual(fake_player_points_label_mock.config.call_count, 0)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
