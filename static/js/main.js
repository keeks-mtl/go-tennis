$(document).ready(function(){
    // delete coach modal function
    // $("#delete-modal").on("show.bs.modal", function(event){
        
    //     //Get the button that triggered the modal
    //     let button = $(event.relatedTarget);

    //     // Extract value from custon data-name attribute to link coach_first_name
    //     let name = button.data("name");
    //     $(this).find("#coach-name").text(name);
        
    //     // Extract value from the custom data-* attribute to link the coach_id 
    //     let url = button.data("url");
    //     $(this).find('#confirm-delete').attr('href', url);
    // });
    // delete modal function
    $("#delete-modal").on("show.bs.modal", function(event){
        
        //Get the button that triggered the modal
        let button = $(event.relatedTarget);

        // Extract value from custon data-topic attribute to link delete topic
        let topic = button.data("topic");
        $(this).find("#delete-topic").text(topic);

        // Extract value from custon data-name attribute to link topic name
        let name = button.data("name");
        $(this).find("#topic-name").text(name);
        
        // Extract value from the custom data-* attribute to link the coach_id 
        let url = button.data("url");
        $(this).find('#confirm-delete').attr('href', url);
    });
});