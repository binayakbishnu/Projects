import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    theme: ThemeData(
      brightness: Brightness.dark,
      primaryColor: Colors.black,
      accentColor: Colors.grey[500],
    ),
    home: todoList(),
  ));
}

class todoList extends StatefulWidget {
  const todoList({Key key}) : super(key: key);

  @override
  _todoListState createState() => _todoListState();
}

class _todoListState extends State<todoList> {
  List tasks = List();
  String input = "";
  bool checkedornot = false;

  @override
  void initState() {
    super.initState();
    tasks.add("task1: ");
    tasks.add("task2: ");
    tasks.add("task3: ");
    tasks.add("task4: ");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("My To-Do List"),
        centerTitle: true,
      ),

      // ADD BUTTON BOTTOM RIGHT
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          showDialog(
              // context: context,
              builder: (BuildContext context) {
                // THE POP-UP
                return AlertDialog(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(5.0),
                    ),

                    // TEXT IN POP-UP
                    title: Text("Enter task"),

                    // INPUT PART IN POP-UP
                    content: TextField(
                      onChanged: (String value) {
                        input = value;
                      },
                    ),

                    // ADD BUTTON IN POP-UP
                    actions: <Widget>[
                      FlatButton(
                        onPressed: () {
                          setState(() {
                            tasks.add(input);
                          });

                          // IMPORTANT!!!!
                          // POP-UP REMOVED
                          Navigator.of(context).pop();
                          // WHY INSIDE OnPressed???
                        },
                        child: Text("Add"),
                      ),
                    ]);
              });
        },

        // PLUS ICON ON BUTTON
        /*child: Icon(
          Icons.add,
          color: Colors.white,
        ),*/

        // TEXT ON THE BUTTON
        child: Text(
          "Add Task",
          textAlign: TextAlign.center, //ALIGNING TO CENTER
          style: TextStyle(

            //HOW TO ADD FONT-FAMILY????

            fontWeight: FontWeight.bold,
            fontSize: 12,
          ),
        ),
      ),

      // MAIN CONTENT
      body: ListView.builder(
          itemCount: tasks.length,
          itemBuilder: (BuildContext context, int index) {
            return Dismissible(
                key: Key(tasks[index]),
                child: Card(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(60.0),
                  ),
                  child: ListTile(

                    // ANY PLACE ON CARD CAN ACTIVATE CHECKBOX
                    onTap: () {
                      setState(() {
                        this.checkedornot = !checkedornot;
                        // IF "!" NOT USED ONTAP AND ONCHANGED CONTRADICT
                      });
                    },

                    // CHECKBOX
                    leading: Checkbox(
                      value: checkedornot,
                      onChanged: (bool value) {
                        setState(() {
                          checkedornot = value;
                        });
                      },
                    ),

                    // THE MAIN TEXT IN TASK
                    title: Text(tasks[index]),

                    // TRAILING
                    trailing: IconButton(
                        icon: Icon(
                          Icons.delete,
                          color: Colors.white,
                        ),
                        onPressed: () {
                          setState(() {
                            tasks.removeAt(index);
                          });
                        }),
                  ),
                ));
          }),
    );
  }
}
