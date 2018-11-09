function ValidationEvent() {
      var title = document.forms["addForm"]["title"].value;
      var subtitle = document.forms["addForm"]["subtitle"].value;
      var content = document.forms["addForm"]["content"].value;
      if (title == "") {
        alert("Title cannot be empty");
        return false;
      }
      if (subtitle == "") {
        alert("Subtitle cannot be empty");
        return false;
      }
      if (content == "") {
        alert("Contact cannot be empty")
        return false
      }
}