#include <iostream>
#include "include/timer.h"
#include "include/utils.h"
#include "include/menu.h"

using namespace std;

int main() {
    while (true){
        switch (welcoming()){
            case 1:
            clearConsole();
            int i = ciclos();
            clearConsole();
                while (i> 0){
                    cout << "Ciclo Nro. "<< i << endl;
                    timer(1);
                    timer(1);
                    i--;
                } 
                
        }
    }
    
}