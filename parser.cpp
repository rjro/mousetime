#include <iostream>
#include "json.hpp"
#include <fstream>
#include <string>


using namespace std;
using json = nlohmann::json;


int main() {
    cout << "Hey there123!!!!" << endl;

    json j;
    
    ifstream ifs("times_map.json");
    ifs >> j;
    
    for ( auto it: j.items() )
    {
        std::cout << it.key() << " | " << it.value() << "\n";   
    }
    // cout << j.dump() << endl;    
    return 0;
}