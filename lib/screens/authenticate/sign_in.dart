import 'package:flutter/material.dart';
// import 'package:appdev_project/services/auth.dart';
// import 'package:firebase_core/firebase_core.dart';

class SignIn extends StatefulWidget {
  // await Firebase.initializeApp();
  @override
  _SignInState createState() => _SignInState();
}

class _SignInState extends State<SignIn> {
  // final AuthService _auth = AuthService();
  //class from auth.dart called
  //can assess signInAnon by _auth.signInAnon

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.brown[100],
      appBar: AppBar(
        backgroundColor: Colors.brown[400],
        elevation: 0.0,
        title: Text('Sign-In'),
      ),
      body: Container(
        padding: EdgeInsets.symmetric(vertical: 20.0, horizontal: 50.0),
        child: RaisedButton(
          child: Text('Sign-In Anon'),
          onPressed: () async {
            // dynamic result = await _auth.signInAnon();
            print('Hello!!');
          },
        ),
      ),
    );
  }
}
