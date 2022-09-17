from PyQt6.QtWidgets import QProgressBar

class ProgressBar(QProgressBar):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setMaximum(100)
    self._active = False

  def updateBar(self, i):
    value = self.value() + i
    self.setValue(value)
    if value >= self.maximum():
      self.setValue(100)