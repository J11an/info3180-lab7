<template>
    <div class="container">

        <form @submit.prevent="uploadPhoto" enctype="multipart/form-data" id = "uploadForm">
        <label for = "description">Description</label>
        <textarea name="description" id="" cols="30" rows="10" class="form-control"></textarea>
        <label for = "photo">Photo</label>
        <input type = "file" name = "photo" class ="form-control">
        <br>
        <button class="btn-primarty" type = "submit">Submit</button>

        </form>

    </div>
</template>

<script>

export default{

    data(){

        return {

            csrf_token : ''
        }
    },

    created(){

        this.getCsrfToken();

    },

    methods:
    {

  

        uploadPhoto(){

            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("api/upload",{
                method: 'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken' : this.csrf_token
                }
            })

            .then(function(response){
                
                return response.json()
            })

            .then(function(data){

                console.log(data)

            })

            .catch(function(error){

                console.log(error)
            });
        },

        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response)=>response.json())
            .then((data)=>{
                console.log(data);
                self.csrf_token = data.csrf_token;
            })

        }
        
    }
}

</script>

<style>
</style>