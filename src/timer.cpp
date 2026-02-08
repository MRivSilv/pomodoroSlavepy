#include <iostream>
#include <chrono>
#include <thread>
#include "../include/timer.h"
using namespace std;

void timer(int minutos){
    int segundos;
    segundos = minutos * 60;
    while (segundos > 0) {
        int m, s;
        m = segundos / 60;
        s = segundos % 60;
        if (s>10){
            cout<< m << ":"<< s << "\r" <<flush;
        }
        else {
            cout<< m << ":0"<< s << "\r" <<flush;
        }
        segundos--;
        this_thread::sleep_for(chrono::seconds(1));
        }

}
