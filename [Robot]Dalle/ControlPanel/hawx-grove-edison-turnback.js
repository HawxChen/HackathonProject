var five = require("johnny-five");
var Edison = require("edison-io");
var board = new five.Board({
  io: new Edison()
});

board.on("ready", function() {
  var a = new five.Motor({
    controller: "GROVE_I2C_MOTOR_DRIVER",
    pin: "A",
  });

  var b = new five.Motor({
    controller: "GROVE_I2C_MOTOR_DRIVER",
    pin: "B",
  });


//  this.wait(1000, function() {
  this.wait(2250, function() {
      console.log("STOP");
      a.stop();
      b.stop();

      this.wait(1000, function() {
        process.emit("SIGINT");
    }.bind(this));
  }.bind(this));

  console.log("turn2 ");
  a.rev(255);
  b.fwd(255);
});

/* @markdown
For this program, you'll need:

![Intel Edison Arduino Breakout](https://cdn.sparkfun.com//assets/parts/1/0/1/3/9/13097-06.jpg)


![Grove Base Shield v2](http://www.seeedstudio.com/depot/images/product/base%20shield%20V2_01.jpg)

(Or similiar Grove shield and platform)

![Grove - I2C Motor Driver](http://www.seeedstudio.com/depot/images/product/12Cmotor_01.jpg)

@markdown */
