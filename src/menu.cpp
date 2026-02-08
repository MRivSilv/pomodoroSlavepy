#include <iostream>
#include "../include/menu.h"
using namespace std;

int welcoming(){
    int decision;
    cout <<"Bienvenido esclavo"<<endl;
    cout <<"1)Pomodoro Standard\n2)Personalizado"<<endl;
    cin >> decision;
    return decision;
}

int ciclos(){
    int c;
    cout << "Elija cantidad de ciclos" << endl;
    cin >> c;
    return c;
}