#-------------------------------------------------
#
# Project created by QtCreator 2016-04-25T21:55:42
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = MOTION-PRESENTATION
TEMPLATE = app

SOURCES += main.cpp\
        widget.cpp \
    event.cpp

HEADERS  += widget.h \
    include/Leap.h \
    include/LeapMath.h \
    event.h \
    error_code.h

FORMS    += widget.ui


unix|win32: LIBS += -L$$PWD/lib/x64/ -lLeap

INCLUDEPATH += $$PWD/lib/x64
DEPENDPATH += $$PWD/lib/x64

unix|win32: LIBS += -L$$PWD/lib/x86/ -lLeap

INCLUDEPATH += $$PWD/lib/x86
DEPENDPATH += $$PWD/lib/x86

RESOURCES += \
    picture.qrc \
    json.qrc

DISTFILES += \
    event_keyboard.json
