import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  //? For Top icons
  List<IconData> _topicons = [
    FontAwesomeIcons.yahoo,
    FontAwesomeIcons.plane,
    FontAwesomeIcons.bed,
    FontAwesomeIcons.walking,
    FontAwesomeIcons.biking,
  ];

  //? function returns a Widget
  Widget _buildTopIcons(int index) {
    return Container(
      //?Big circle
      height: 60.0,
      width: 60.0,
      decoration: BoxDecoration(
        color: Colors.blueGrey[100],
        borderRadius: BorderRadius.circular(30.0),
      ),
      child: Icon(
        _topicons[index],
        color: Colors.blueGrey[500],
        // color: Theme.of(context).accentColor,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[400],
      appBar: AppBar(
        backgroundColor: Color.fromRGBO(0, 0, 0, 0.0),
        // title: Text('HOME'),
        // centerTitle: true,
        // title: TextField(
        //   decoration: InputDecoration(
        //     border: OutlineInputBorder(),
        //     hintText: 'Enter a search term',
        //   ),
        // ),

        title: TextFormField(
          // onChanged: (text) {
          //   print('First text field: $text');
          // },

          onTap: () {
            FocusScopeNode currentFocus = FocusScope.of(context);

            if (!currentFocus.hasPrimaryFocus) {
              currentFocus.unfocus();
            }
          },

          decoration: InputDecoration(
            labelText: 'Search',
            hintText: 'Start typing or tap to close',
            // fillColor: Colors.grey,
            // borderRadius: BorderRadius.circular(8.0),

            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(
                color: Colors.black,
                width: 2.0,
              ),
            ),

            // focusColor: Colors.grey[200],
            focusedBorder: OutlineInputBorder(
              gapPadding: 10.0,
              borderRadius: BorderRadius.circular(5.0),
              // borderSide: BorderSide(width: 1, color: Colors.black),
              borderSide: BorderSide(
                // color: Colors.grey[900],
                color: Color.fromRGBO(85, 85, 85, 1.0),
                width: 1.0,
              ),
            ),
          ),

          // validator: (String? value) {
          //   return (value != null && value.contains('@'))
          //       ? 'Do not use the @ char.'
          //       : null;
          // },
        ),
        elevation: 0,
      ),
      // body: Container(
      //   child: Column(
      //     // mainAxisAlignment: MainAxisAlignment.center,
      //     // crossAxisAlignment: CrossAxisAlignment.stretch,
      //     children: [
      //       Container(
      //         child: Text('Hello'),
      //       ),
      //       RaisedButton(
      //         onPressed: () {},
      //         child: Text('Button'),
      //       ),
      //     ],
      //   ),
      // ),
      // child: Text('Hello'),
      // child: RaisedButton(
      //   onPressed: () {},
      //   child: Text('Button'),
      // ),
      body: SafeArea(
        child: ListView(
          padding: EdgeInsets.symmetric(vertical: 30.0),
          children: <Widget>[
            Padding(
              padding: EdgeInsets.only(left: 20.0, right: 120.0),
              child: Text(
                'Find your place',
                style: TextStyle(
                  backgroundColor: Colors.grey[300],
                  fontSize: 30.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            SizedBox(height: 20.0), //! add space
            Row(
              // children: <Widget>[
              //   _buildTopIcons(0),
              //   _buildTopIcons(1),
              //   _buildTopIcons(2),
              //   _buildTopIcons(3),
              // ],
              children: _topicons
                  .asMap() //? mapping to that new members dynamically added
                  .entries
                  .map((MapEntry map) =>
                      _buildTopIcons(map.key)) //? map.key is index
                  //? iterates whole list to create map
                  .toList(), //? need to convert map to list since children is a list
            ),
          ],
        ),
      ),
    );
  }
}
