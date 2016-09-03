var user_id = 1;  // 用户的唯一标识符
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/maillist/syn/");
chat_socket.onopen = function() {
  var data = {
    send_type: 'connect',
    user_id: user_id,
  };
  chat_socket.send(JSON.stringify(data));
  return false;
};

chat_socket.onmessage = function(message) {
  var data = JSON.parse(message.data);
  if(data.result == 'fail') {
    alert(data.msg);
  };
  if(data.result == 'choice') {
    if (confirm(data.msg) == true) {
      data.data.old_data = data.last_data;
      data.last_data = null;
      chat_socket.send(JSON.stringify(data));
    };
  };
  if(data.result != 'fail') {
    synchro();  // 这里本来是传回了对应的同步数据的，逻辑写起来麻烦，统一刷新了
  };
  $('#chat').append('<div>' + message.data + '</div>');
};

function chatsock() {
  var status = $(this).attr('id');
  var message = {
    status: status,
    user_id: user_id,
    info_id: parseInt($('#info_id').val()),
    name: $('#name').val(),
    phone: parseInt($('#phone').val()),
    send_type: 'send_info',
  };
  if(status == 'change') {
    var old_data = $('.info_' + $('#info_id').val());
    message['old_data'] = {
      name: old_data.first().next().text(),
      phone: parseInt(old_data.last().text()),
    };
  };
  chat_socket.send(JSON.stringify(message));
  synchro();
  return false;
}


function synchro() {
  $.post('/synchro/', $('form').serializeArray(), function(datas) {
      $('table').html('');
      $.each(datas.contacts, function(index) {
        $('table').append('<tr><td class="info_' + this.info_id + '">' + this.info_id + '</td><td class="info_' + this.info_id + '">' + this.name + '</td><td class="info_' + this.info_id + '">' + this.phone + '</td></tr>');

      });
      return false;
  }, 'json');
  return false;
}

$(function () {
  $('#add').click(chatsock);
  $('#delete').click(chatsock);
  $('#change').click(chatsock);
  synchro();
  return false;
});
