#include "widget.h"
#include "ui_widget.h"
#include <QApplication>
#include <QDesktopWidget>
#include <QPalette>
#include <Windows.h>
#include <QTimer>
#include <iostream>


#pragma comment (lib,"Advapi32.lib")
#pragma comment (lib,"User32.lib")
Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    //set Geometry (-60,-60) from Right-Buttom, size is 180*180
    this->setGeometry(QApplication::desktop()->width()-240,QApplication::desktop()->height()-240,180,180);

    //set Window Background Color R0:G0:B0 (BLACK), Opacity is 0.8
    this->setPalette(QPalette( QColor(0, 0, 0)) );
    this->setWindowOpacity(0.8);

    //set Window Flag : Tool | Frameless | Stay On Top
    this->setWindowFlags(Qt::Tool | Qt::FramelessWindowHint | Qt::WindowStaysOnTopHint);

    //TRANSPARENT and LAYERED for Windows
    SetWindowLong((HWND)winId(), GWL_EXSTYLE, GetWindowLong((HWND)winId(), GWL_EXSTYLE) |
                  WS_EX_TRANSPARENT | WS_EX_LAYERED);

    QTimer *direction_timer = new QTimer(this);
    connect(direction_timer,SIGNAL(timeout()),this,SLOT(update()));
    direction_timer->start(500);

    controller.setPolicy(Leap::Controller::POLICY_BACKGROUND_FRAMES);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::setDirectionDisplay(QString direction_type)
{
    //the resource path
    QString picture_path = "\":/resource/";
    QString picture_name = direction_type;
    //set up the style sheet
    QString direction_label_css = "#direction_show_label{border-image: url(" + picture_path + picture_name + ".png\");}";
    this->setStyleSheet(direction_label_css);
}

void Widget::update()
{
    Leap::Vector hand_speed = controller.frame().hands()[0].fingers()[1].tipVelocity();
    double threshold = 200.0;
    if(hand_speed.x > threshold/2){
        this->setDirectionDisplay("right");
        event.keyboardType("RIGHT");
        return;
    }
    if(hand_speed.x < -threshold/2){
        this->setDirectionDisplay("left");
        event.keyboardType("LEFT");
        return;
    }
    if(hand_speed.y > threshold){
        this->setDirectionDisplay("up");
        event.keyboardType("UP");
        return;
    }
    if(hand_speed.y < -threshold){
        this->setDirectionDisplay("down");
        event.keyboardType("DOWN");
        return;
    }
}
