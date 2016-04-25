#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "include/Leap.h"
#include "event.h"
namespace Ui {
    class Widget;
}

class Widget : public QWidget
{
        Q_OBJECT

    public:
        explicit Widget(QWidget *parent = 0);
        ~Widget();

    public slots:
        void setDirectionDisplay(QString direction_type);
        void update();

    private:
        Ui::Widget *ui;
        Leap::Controller controller;
        Event event;
};

#endif // WIDGET_H
