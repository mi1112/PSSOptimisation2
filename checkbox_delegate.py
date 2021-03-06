from PyQt4.QtCore import QEvent, Qt, QRect, QPoint, QVariant
from PyQt4.QtGui import QStyleOptionButton, QStyle, QApplication
from PyQt4.QtGui import QStyledItemDelegate

class CheckBoxDelegate(QStyledItemDelegate):
    """This delegate paints bool type cells as checkboxes."""

    def createEditor(self, parent, option, index):
        """Important, otherwise an editor is created if the user clicks in this
        cell.
        """
        if index.data().type() != QVariant.Bool:
            return super(CheckBoxDelegate, self).createEditor(parent, option, index)

    def paint(self, painter, option, index):
        """Paint a checkbox without the label if the index contains a bool,
        do the default otherwise.
        """
        if index.data().type() != QVariant.Bool:
            return super(CheckBoxDelegate, self).paint(painter, option, index)

        checked = index.data().toBool()
        check_box_style_option = QStyleOptionButton()

        # draw disabled and read-only if flag not set
        if bool(index.flags() & Qt.ItemIsEnabled):
            check_box_style_option.state |= QStyle.State_Enabled
        # if enabled, check if it is editable
        else:
            if not bool(index.flags() & Qt.ItemIsEditable):
                check_box_style_option.state |= QStyle.State_ReadOnly

        if checked:
            check_box_style_option.state |= QStyle.State_On
        else:
            check_box_style_option.state |= QStyle.State_Off

        check_box_style_option.rect = self.getCheckBoxRect(option) 

        QApplication.style().drawControl(QStyle.CE_CheckBox,
            check_box_style_option, painter)


    def editorEvent(self, event, model, option, index):
        """Change the data in the model and the state of the checkbox if the
        user presses the left mousebutton or presses Key_Space or Key_Select
        and this cell is editable. Otherwise do nothing.
        """
        if int(index.flags() & Qt.ItemIsEditable) == 0 or \
            int(index.flags() & Qt.ItemIsEnabled) == 0:
            return False

        # Do not change the checkbox-state
        if event.type() == QEvent.MouseButtonRelease or \
            event.type() == QEvent.MouseButtonDblClick:
            if event.button() != Qt.LeftButton or \
                not self.getCheckBoxRect(option).contains(event.pos()):
                return False
            if event.type() == QEvent.MouseButtonDblClick:
                return True
        elif event.type() == QEvent.KeyPress:
            if event.key() != Qt.Key_Space and event.key() != Qt.Key_Select:
                return False
        else:
            return False

        # Change the checkbox-state
        self.setModelData(None, model, index)
        return True

    def setModelData (self, editor, model, index):
        """The user wanted to toggle the checkbox."""
        new_value = not index.data().toBool()
        model.setData(index, new_value, Qt.EditRole) 

    def getCheckBoxRect(self, option):
        check_box_style_option = QStyleOptionButton()
        check_box_rect = QApplication.style().subElementRect(
            QStyle.SE_CheckBoxIndicator, check_box_style_option, None)
        check_box_point = QPoint (option.rect.x() +
                             option.rect.width() / 2 -
                             check_box_rect.width() / 2,
                             option.rect.y() +
                             option.rect.height() / 2 -
                             check_box_rect.height() / 2)
        return QRect(check_box_point, check_box_rect.size())
