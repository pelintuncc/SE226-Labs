#include <iostream>
using namespace std;


class Node{
public:
    int data;
    Node *next;

    Node (int data , Node *next ){
        this->data = data;
        this->next = next;
    }
};


class Stack{
private:
    Node *beginningNode;
    int stack_size;

public:
    Stack(){
        beginningNode = nullptr;
        stack_size = 0;
    }



    void push(int x){
        if (beginningNode == nullptr) {
            beginningNode = new Node(x, nullptr);
        }
        else {
            Node *temp = beginningNode;
            beginningNode = new Node(x, temp);
        }


    }
    int top(){
        return beginningNode->data;
    }
    int pop(){

        if(size() == 0){
            cout << "Your stack is empty";
        }
        else {

            int topData = top();
            beginningNode = beginningNode->next;
            stack_size--;
            return topData;
        }

    }


    bool isEmpty(){
        if(stack_size == 0){
            return true;
        }
        else{
            return false;
        }
    }
    int size(){
        return stack_size;
    }
    void print(){


        Node *temp;
        for(temp=beginningNode; temp!=nullptr; temp=temp->next) {
            cout << temp->data << " ";
        } cout << endl;
    }
    


};

int main(){

    Stack *my_stack = new Stack();


    bool flag = true;

    while (flag) {
        cout<< "\n1. Push in to stack \n2. Pop out from the stack \n3. Print the stack size \n4. Print the whole stack  \n5. Exit from the program." << endl;

        int input;
        cin >> input;

        switch (input) {


            case 1:
                int pushInput;
                cout << "Please enter a number: ";
                cin >> pushInput;
                my_stack->push(pushInput);

                break;

            case 2:
                if(my_stack->size() == 0 ){
                    my_stack->pop();
                    break;
                }
                else {
                    my_stack->pop();
                    cout << "Your new stack: ";
                    my_stack->print();
                    break;
                }

            case 3:
                my_stack->size();
                break;


            case 4:
                cout << "Your stack is: ";
                my_stack->print();
                break;


            case 5:
                flag = false;

        }
    }
    return 0;
};

