from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QIcon
import sys

app = QApplication(sys.argv)

# Create a QWidget
window = QWidget()
window.setWindowTitle('My Screenmate')
window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
window.resize(600, 400)
window.setAttribute(Qt.WA_TranslucentBackground)

label = QLabel(window)
label.resize(600, 400)
window.move(1400, 712)

# Create a QMovie object
movie = QMovie('mate.gif')

# Set the movie to QLabel
label.setMovie(movie)

# Start the GIF
movie.start()

# Create System Tray Icon
tray_icon = QSystemTrayIcon(QIcon('gear.ico'), parent=app)
tray_icon.setToolTip('My Screenmate')

# Create a menu for the tray icon
tray_menu = QMenu()
exit_action = QAction('Exit', tray_menu)
exit_action.triggered.connect(app.quit)
tray_menu.addAction(exit_action)

# Set the menu
tray_icon.setContextMenu(tray_menu)

# Show the tray icon
tray_icon.show()

# Show the window
window.show()

# Close the application when clicked
def close(event):
    app.quit()

label.mousePressEvent = close

sys.exit(app.exec_())