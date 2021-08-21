#include<bits/stdc++.h>
#include<iostream>

struct Node{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

using namespace std;

void preorder(struct Node* root){
    if (root == NULL){
        return;
    }
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

void inorderTraversal(struct Node* root){
    if (root == NULL){
        return;
    }
    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}

void postorder(struct Node* root){
    if (root == NULL){
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " ";
}

int search(int inorder[], int start, int end, int curr){
    for(int i=start;i<=end;i++){
        if (inorder[i] == curr){
            return i;
        }
    }
    return -1;
}

Node* buildTree(int preorder[], int inorder[], int start, int end){
    static int idx = 0;
    if (start > end){
        return NULL;
    }

    int curr = preorder[idx];
    Node* node = new Node(curr);
    idx++;

    int pos = search(inorder, start, end, curr);
    node->left = buildTree(preorder, inorder, start, pos-1);
    node->right = buildTree(preorder, inorder, pos+1, end);

    return node;
}

Node* buildTree2(int postorder[], int inorder[], int start, int end){
    static int idx = end;
    if (start > end){
        return NULL;
    }

    int val = postorder[idx];
    idx--;
    Node* curr = new Node(val);

    if (start == end){
        return curr;
    }

    int pos = search(inorder, start, end, val);
    curr->right = buildTree2(postorder, inorder, pos+1, end);
    curr->left = buildTree2(postorder, inorder, start, pos-1);
    return curr;

}

void printLevelOrder(Node* root){
    if (root == NULL){
        return;
    }
    queue<Node *> q;
    q.push(root);
    q.push(NULL);

    while (!q.empty())
    {
        Node* node = q.front();
        q.pop();
        if (node != NULL){
            cout << node->data << " ";

            if (node->left)
                q.push(node->left);
            if (node->right)
                q.push(node->right);
            
        }
        else if(!q.empty()){
            q.push(NULL);
        }
    }    
}

int sumAtK(Node* root, int K){
    if (root == NULL){
        return -1;
    }

    queue<Node *> q;
    q.push(root);
    q.push(NULL);
    int level = 0;
    int sum = 0;

    while(!q.empty()){
        Node * node = q.front();
        q.pop();

        if (node != NULL){
            if (level == K){
                sum += node->data;
            }
            if (node->left)
                q.push(node->left);
            if (node->right)
                q.push(node->right);
        }
        else if(!q.empty()){
            q.push(NULL);
            level++;
        }
    }
    return sum;
}

int countNodes(Node* root){
    if (root == NULL){
        return 0;
    }
    return countNodes(root->left) + countNodes(root->right) + 1;
}

int sumNodes(Node* root){
    if (root == NULL){
        return 0;
    }
    return sumNodes(root->left) + sumNodes(root->right) + root->data;
}

int calcHeight(Node* root){
    if (root == NULL){
        return 0;
    }
    int lHeight = calcHeight(root->left);
    int rHeight = calcHeight(root->right);
    return lHeight + rHeight + 1;
}

int main(){

    
    struct Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);

    root->left->left = new Node(4);
    root->left->right = new Node(5);

    root->right->left = new Node(6);
    root->right->right = new Node(7);

    /*
    preorder(root);
    cout << endl;
    inorder(root);
    cout << endl;
    postorder(root);
    */

   /*
    int preorder[] = {1,2,4,3,5};
    int inorder[] = {4,2,1,5,3};
    int postorder[] = {4,2,5,3,1};

    // Node* root = buildTree(preorder, inorder, 0, 4);
    Node* root = buildTree2(postorder, inorder, 0, 4);
    inorderTraversal(root);
    */

    //   printLevelOrder(root);

    // cout<<sumAtK(root, 2);

    // cout << countNodes(root) << " " << sumNodes(root);

    cout << calcHeight(root) << " ";

    return 0;
}
