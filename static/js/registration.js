$(document).ready(function(){
    // For date picker
    $('.datepicker').datepicker({ format: "dd-mm-yyyy",autoclose:true, });
    $("form[id='registration']").validate({
        // Specify validation rules
         onkeyup: true,
        //by default the error elements is a <label>
        errorElement: "label",
        //place all errors in a <div id="errors"> element
        errorPlacement: function(error, element) {
            error_elem = element.parent().find("span.error");
            error_elem.html("");
            error.appendTo(error_elem);            
        },
        rules: {
            first_name:{
                required : true
            },
            last_name: {
                required: true,
            },
            date_of_birth: {
                required: true,
            },
            address: {
                required: true,
            },
            contact_number: {
                required: true,
                digits: true,
                maxlength: 10
            },
            hieght: {
                required: true,
            },
            email: {
                required: true,
            },
            education: {
                required: true,
            },
            employment: {
                required: true,
            },
            about_you: {
                required: true,
            },

        },
        // Specify validation error messages
        messages: {
            first_name:{
                required : "Please select First Name."
            },
            last_name: {
                required: "Please select Last Name.",
            },
            date_of_birth: {
                required: "Please enter DOB.",
                minlength: 5
            },
            address: {
                required: "Please select Address.",
            },
            contact_number: {
                required: "Please select Contact Number.",
            },
            hieght: {
                required: "Please select Height.",
            },
            email: {
                required: "Please select Valid email.",
            },
            education: {
                required: "Please enter Education.",
            },
            employment: {
                required: "Please enter Employment.",
            },
            about_you: {
                required: "Please enter Your details.",
            }
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
            
        }
    });
});
