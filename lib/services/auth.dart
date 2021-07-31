import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_auth_web/firebase_auth_web.dart';

class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;

  //anon sign in
  Future signInAnon() async {
    try {
      UserCredential result = await _auth.signInAnonymously();
      User? user = result.user;
      return user;
    } catch (e) {
      print(e.toString());
      return null;
    }
  }

  //email/password sing in

  //register with email/password

  //signout
}
