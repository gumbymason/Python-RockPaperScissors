wins = 0
losses = 0
ties = 0






__version__ = '0.1'
__author__ = 'Mason Grant'

# Create the Controller for the app
class RPSCtrl:
    """Controller"""
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectSignals()
    
    def _rock(self):
        """Player Chose Rock"""
        global ties, wins, losses
        choice = self._model.CPUChoice()
        if choice == 'Rock':
            winner = 'It\'s a tie.'
            ties += 1
        elif choice == 'Scissors':
            winner = 'You win.'
            wins += 1
        elif choice == 'Paper':
            winner = 'I win!'
            losses += 1
        message = 'You chose Rock, I chose ' + choice + '. ' + winner
        self._view.setDisplayText(message)
        self._view.setTotalsDisplay(wins, losses, ties)
    
    def _paper(self):
        """Player Chose Paper"""
        global ties, wins, losses
        choice = self._model.CPUChoice()
        if choice == 'Paper':
            winner = 'It\'s a tie.'
            ties += 1
        elif choice == 'Rock':
            winner = 'You win.'
            wins += 1
        elif choice == 'Scissors':
            winner = 'I win!'
            losses += 1
        message = 'You chose Paper, I chose ' + choice + '. ' + winner
        self._view.setDisplayText(message)
        self._view.setTotalsDisplay(wins, losses, ties)
    
    def _scissors(self):
        """Player Chose Scissors"""
        global ties, wins, losses
        choice = self._model.CPUChoice()
        if choice == 'Scissors':
            winner = 'It\'s a tie.'
            ties += 1
        elif choice == 'Paper':
            winner = 'You win.'
            wins += 1
        elif choice == 'Rock':
            winner = 'I win!'
            losses += 1
        message = 'You chose Scissors, I chose ' + choice + '. ' + winner
        self._view.setDisplayText(message)
        self._view.setTotalsDisplay(wins, losses, ties)

    def _connectSignals(self):
        """Connect Signals and slots"""
        self._view.buttons['Rock'].clicked.connect(lambda: self._rock())
        self._view.buttons['Paper'].clicked.connect(lambda: self._paper())
        self._view.buttons['Scissors'].clicked.connect(lambda: self._scissors())